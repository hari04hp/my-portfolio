# Used hugging face embedding, so embeddings are free.
from streamlit_lottie import st_lottie
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="About My AI Assistant", page_icon="🤖", layout="wide")
st.markdown("""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
            """, unsafe_allow_html=True)
with open('assets/css/styles.css') as f:
        st.markdown(f"""<style>{f.read()}""", unsafe_allow_html=True)

st.header("My AI Assistant in my portfolio")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
ml_lottie = load_lottieurl("https://lottie.host/30f7a673-5d1a-4a83-b694-0361c985b506/Ik5pQjtkjb.json")


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
        dict_of_lotties = {"python": python_lottie, "mysql": my_sql_lottie, "ml": ml_lottie}
        columns = st.columns(len(dict_of_lotties))
        for index,column in enumerate(columns):
            with column:
                st_lottie(dict_of_lotties[list(dict_of_lotties.keys())[index]], height=70,width=70, key=list(dict_of_lotties.keys())[index], speed=2.5)

st.subheader("Project Overview")
st.write("""The objective is to develop a chat assistant using Retrieval Augmentaion with Langchain which learns about me with my resume and will try to answer the relevant questions that are raised.""")
st.write("The project is hosted at [Streamlit](https://haripriya-rajendran-portfolio.streamlit.app/2_My_Assistant) and the scripts are at [GitHub](https://github.com/hari04hp/my-portfolio)")

st.subheader("Technologies Used")
st.write("""
        1. Streamlit
        2. Langchain
        3. OpenAI API
        4. PineCone Vector Database
        5. HuggingFaceEmbeddings
        """)

st.subheader("Project Details")
st.write("""Streamlit is the framework used to host my web application. I used Langchain framework to easily access mutliple other frameworks.""")
st.write("""
         1. Initially, I uploaded my resume pdf to a folder.
         2. Then, I have created the Embeddings for the pdf using HuggingFaceEmbeddings.
         3. I have stored the embeddings as vectors to the Pinecone Vector database.
         4. Once the index is created, I created a chatbot page using streamlit.
         5. Fetched the index from pinecone and is provided as a context to the prompt.
         6. The LLM model used here is ***gpt-3.5-turbo-0125*** from OpenAI.
         7. I also have configured ConversationalBufferMemory to maintain and use the chat history in prompts.
         8. Session is also maintained to show the chat history.
         9. Chat history messages are stored in sqllite.
""")

st.subheader("Demo Video")
video_file = open('images/demo_video_2.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.subheader("FAQ")
st.write("""***Why did I use ConversationalBufferMemory instead of ConversationalSummaryMemory?***""")
st.write("""Because, ConversationalBufferMemory takes less number of tokens for short conversation. Only when the conversation goes longer, ConversationalSummaryMemory takes lesser number of tokens. Reference graph below.""")
st.image("images/memory.png", width = 800)


st.subheader("How to use?")
st.write("""
    1. Type any query/prompt that you need to know about me to the chatbot.
    2. The code already limits the response to 50 words. If you want to limit the words or add the number of words, please mention it along with the query. But, because of the GPT's drawback of not being able to count the words properly. The word count might get higher. With testing, I found that it mostly did not exceed the 50 words limit I have povided here.
    3. It uses the context I have given and will reply in sometime.
    4. As simple as that!
    5. Please be aware of the disclaimer that Using this chatbot can cost around \\$0.01 to \\$0.05 per query (depends on the query). It also stores and uses the previous questions to prompt each question. So, use it based on your available OpenAI API quota.
""")

st.subheader("Queries or suggestions?")
st.write("""Contact me on [Linkedin](https://www.linkedin.com/in/haripriyar)""")

