import requests
import streamlit as st
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone as pc_vector
from langchain.chains import ConversationalRetrievalChain
from langchain.callbacks.base import BaseCallbackHandler
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_openai import ChatOpenAI
from openai import AuthenticationError
import os
from streamlit_lottie import st_lottie

from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def configure_retriever(index_name):
    # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v1")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    docsearch = pc_vector.from_existing_index(index_name, embeddings)
    retriever = docsearch.as_retriever(search_type="mmr")
    return retriever

class StreamHandler(BaseCallbackHandler):
    '''Class for displaying the streaming the response as soon as it's received.'''
    def __init__(self, container: st.delta_generator.DeltaGenerator, initial_text: str = ""):
        self.container = container
        self.text = initial_text
        self.run_id_ignore_token = None

    def on_llm_start(self, serialized: dict, prompts: list, **kwargs):
        # Workaround to prevent showing the rephrased question as output
        if prompts[0].startswith("Human"):
            self.run_id_ignore_token = kwargs.get("run_id")

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        if self.run_id_ignore_token == kwargs.get("run_id", False):
            return
        self.text += token
        self.container.markdown(self.text)

class PrintRetrievalHandler(BaseCallbackHandler):
    '''Printing the received query and response in a chat format.'''
    def __init__(self, container):
        self.status = container.status("**Context Retrieval**")

    def on_retriever_start(self, serialized: dict, question: str, **kwargs):
        self.status.write(f"**Question:** {question}")
        self.status.update(label=f"**Context Retrieval:** {question}")

    def on_retriever_end(self, documents, **kwargs):
        for idx, doc in enumerate(documents):
            source = os.path.basename(doc.metadata["source"])
            self.status.write(f"**Document {idx} from {source}**")
            self.status.markdown(doc.page_content)
        self.status.update(state="complete")

st.set_page_config(page_title="Haripriya Rajendran - Assistant", page_icon="🤖", layout="wide")
st.markdown("""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
            """, unsafe_allow_html=True)
with open('assets/css/styles.css') as f:
        st.markdown(f"""<style>{f.read()}""", unsafe_allow_html=True)

st.header("My AI Assistant 🤖")
with st.container():
    openai_api_key = st.sidebar.text_input(
        label="Enter your OpenAI API key", type="password"
    )
    username = st.sidebar.text_input(
        label="Enter your username"
    )
    if not openai_api_key.startswith('sk-') or not username:
        # st.sidebar.warning("Please add your OpenAI API key to use the chatbot. Username is necessary to maintain chat history.", icon = "ℹ")
        # st.warning("Please add your OpenAI API key to use the chatbot. Username is necessary to maintain chat history.", icon = "ℹ")
        st.info("Please add your OpenAI API key in the sidebar on the left to use the chatbot. Username is also necessary to maintain and retrieve your chat history. Please give a unique id or name if possible. To open sidebar in the mobile, click on the arrow at the top left.", icon = "ℹ")
    
    button_status = st.sidebar.button("Clear message history")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
ml_lottie = load_lottieurl("https://lottie.host/30f7a673-5d1a-4a83-b694-0361c985b506/Ik5pQjtkjb.json")
open_ai_img = "images/openAI.jpg"

with st.container():
    st.sidebar.image("images/my-image-2.jpg")
    st.sidebar.title("Haripriya Rajendran 🤓")
    st.sidebar.header("Data Scientist 👩‍💻")
    
    with st.sidebar:
        columns = st.columns(2)
        columns[i:=0].markdown("""
        <a href="https://github.com/hari04hp" class="text-decoration-none text-light"><i class="fab fa-github contact-icons1" style="font-size: 50px;"></i></a>""",unsafe_allow_html=True,)
        columns[i:=i+1].markdown("""
        <a href="https://www.linkedin.com/in/haripriyar" class="text-decoration-none text-light"><i class="fab fa-linkedin contact-icons1" style="font-size: 50px;"></i></a>""",unsafe_allow_html=True,)
    
    with st.sidebar:
        dict_of_lotties = {"python": python_lottie, "mysql": my_sql_lottie, "ml": ml_lottie, "openAI": open_ai_img}
        columns = st.columns(len(dict_of_lotties))
        for index,column in enumerate(columns):
            with column:
                if index < 3:
                    st_lottie(dict_of_lotties[list(dict_of_lotties.keys())[index]], height=70,width=70, key=list(dict_of_lotties.keys())[index], speed=2.5)
                else:
                    st.image(dict_of_lotties[list(dict_of_lotties.keys())[index]],width=70, )

st.warning("""⚠ ***Disclaimer: Using this chatbot can cost around \\$0.01 to \\$0.05 per query. It also stores and uses the previous questions to prompt each question.***""")


if username and openai_api_key.startswith('sk-'):
    db_path = 'local_sqlite_db.db'
    msgs = SQLChatMessageHistory(
        session_id=username,
        connection="sqlite:///" + db_path  # This is the SQLite connection string
    )
    
    index_name = "my-portfolio"
    memory = ConversationBufferMemory(memory_key="chat_history", chat_memory=msgs, return_messages=True)
    
    # Setup LLM and QA chain
    llm = ChatOpenAI(
        model_name="gpt-4o-mini", openai_api_key=openai_api_key, temperature=0, streaming=True
    )#, max_tokens=35
    
    #with chat history
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.prompts import MessagesPlaceholder
    system_prompt = "You are A CHAT ASSISTANT even with or without context and you are NOT Haripriya. You are supposed to answer the questions asked only about Haripriya and you are NOT Haripriya. Use the following pieces of retrieved context to answer the question.\n\n{context}"
    qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{question}"),
    ]
    )
    
    
    #existing
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm, retriever=configure_retriever(index_name), memory=memory, verbose=True,
        combine_docs_chain_kwargs={"prompt": qa_prompt},
    )
    

    if len(msgs.messages) == 0 or button_status:
        msgs.clear()
        msgs.add_ai_message("I can answer any question about Haripriya Rajendran. How can I help you?")
    avatars = {"human": "user", "ai": "assistant"}
    for msg in msgs.messages:
        st.chat_message(avatars[msg.type]).write(msg.content)
    if user_query := st.chat_input(placeholder="Ask my AI Assistant anything about me!"):
        st.chat_message("user").write(user_query)

        # user_query+=' If the number of words limit is given already, brief the answer into that number. Otherwise, brief it in at most 35 words. '
        user_query += ' Brief it in at most 35 words or the count limit given in the previous sentence.'

        with st.chat_message("assistant"):
            retrieval_handler = PrintRetrievalHandler(st.container())
            stream_handler = StreamHandler(st.empty())
            try:
                # response = qa_chain.run(user_query, callbacks=[retrieval_handler, stream_handler])
                response = qa_chain.invoke({"question":user_query}, {"callbacks" :[retrieval_handler, stream_handler]})
            except AuthenticationError as e:
                if e.code == 'invalid_api_key':
                    st.error("Please enter a valid API key.")
