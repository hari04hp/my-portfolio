### Project is hosted at https://haripriya-rajendran-portfolio.streamlit.app/

## How to run locally:

Upload a file under files

1. ```pip install -r requirements.txt```
2. ```streamlit run 1_Home.py```

Create a .env file in the project directory and add:
* PINECONE_API_KEY=Your Pinecone API key
* PINECONE_ENV=Your Pinecone environment name (e.g., "dev")


## Pages
1. Home page is my portfolio describing about me, Haripriya Rajendran.
2. Second page is "My AI Assistant" page where you can ask relevant questions about me and it will answer.
3. Third page is "About My AI Assistant" page where the project details are described.

## References for both chat assistant and portfolio:
- https://github.com/logesh45/rag-langchain-demo
- https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/chat_with_documents.py
- https://github.com/Sven-Bo/personal-website-streamlit
- https://www.youtube.com/watch?v=VqgUkExPvLY
- https://www.youtube.com/watch?v=u-RLu_8kwA0
- https://blog.streamlit.io/land-your-dream-job-build-your-portfolio-with-streamlit/#step-2-build-your-chatbot
- https://www.pinecone.io/learn/series/langchain/langchain-retrieval-augmentation/

## Hosting path:
https://haripriya-rajendran-portfolio.streamlit.app/

## Licenses:
This project is licensed under the MIT License - see the LICENSE file for details.



# RAG Evaluation
Evaluated the context retrieval and the answer relevance with Non-LLM and LLM evaluations but altering the chunk size, the embedding model, but finally when LLM evaluations were done using deepeval, I found that the contexts were the main issue.

Refer [Old Context Format's Image](images/old_context_format_pdf.png)

You can see that there are so many spacings. This happens in the same way when we copy texts from pdf directly and paste it. This is because PDFs can contain formatting codes that don't translate perfectly when pasted into other applications, leading to extra spaces or line breaks. The same scenario is happening in this pdf conversion to embedding as well. This fogs the actual context retrieval.

So when I convert it to use embeddings created from word document, everything was better. See [New Context Format's Image](images/new_context_format_word_1.png), [New Context Format's Image 2](images/new_context_format_word_2.png)