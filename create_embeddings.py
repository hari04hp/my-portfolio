import os
import sys

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader,  Docx2txtLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone as pc_vector
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

from pinecone import Pinecone, ServerlessSpec
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "my-portfolio"

def create_embeddings(file, doc_extension):
    # Read documents
    docs = []
    if doc_extension == 'pdf':
        loader = PyPDFLoader(file)
    elif doc_extension == 'docx':
        loader = Docx2txtLoader(file)
    else:
        raise Exception("Extension should be docx or pdf")
    # docs.extend(loader.load())
    docs = loader.load()

    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=300)
    splits = text_splitter.split_documents(docs)

    # Create embeddings and store in vectordb
    # Using HuggingFaceEmbeddings because it's free
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v1") #updated from

    # First, check if our index already exists. If it doesn't, we create it
    #pc.delete_index(index_name)
    if not pc.list_indexes():
        # create_index(index_name, docs, embeddings)
        create_index(index_name, splits, embeddings)
    else:
        #for single index checking
        # for each_index in pc.list_indexes():
        #     if index_name != each_index['name']:#pinecone.list_indexes():
        #         # create_index(index_name, docs, embeddings)
        #         create_index(index_name, splits, embeddings)
        #     else:
        #         print("Index already exists.")
        #         break
        #now multiple indices can be created. so changing the check condition
        all_indexes = [d['name'] for d in pc.list_indexes()]
        if index_name in all_indexes:
            print("Index already exists.")
        else:
            create_index(index_name, splits, embeddings)

def create_index(index_name, docs, embeddings):
    # we create a new index
    pc.create_index(name=index_name, metric="cosine", dimension=384, spec = ServerlessSpec(
    cloud="aws", region="us-east-1")) #with starter plan
    docsearch = pc_vector.from_documents(docs, embeddings, index_name=index_name)
    print("Index Created.")

# Specify the directory containing the PDF files
# file = 'files/Resume-Haripriya Rajendran.pdf'
file = 'files/Resume for RAG.docx'
create_embeddings(file, file.split('.')[-1])
index = pc.Index(index_name)
print(index.describe_index_stats())