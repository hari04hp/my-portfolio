import os
import sys

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone as pc_vector

load_dotenv()

from pinecone import Pinecone, ServerlessSpec
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


def create_embeddings(file):
    # Read documents
    docs = []
    index_name = "my-portfolio"
    loader = PyPDFLoader(file)
    docs.extend(loader.load())


    # Create embeddings and store in vectordb
    # Using HuggingFaceEmbeddings because it's free
    # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v1") #updated from

    # First, check if our index already exists. If it doesn't, we create it
    # pc.delete_index(index_name)
    if not pc.list_indexes():
        create_index(index_name, docs, embeddings)
    else:
        for each_index in pc.list_indexes():
            if index_name != each_index['name']:#pinecone.list_indexes():
                create_index(index_name, docs, embeddings)
            else:
                print("Index already exists.")
                break

def create_index(index_name, docs, embeddings):
    # we create a new index
    pc.create_index(name=index_name, metric="cosine", dimension=384, spec = ServerlessSpec(
    cloud="aws", region="us-east-1")) #with starter plan
    docsearch = pc_vector.from_documents(docs, embeddings, index_name=index_name)
    print("Index Created.")

# Specify the directory containing the PDF files
file = 'files/Resume-Haripriya Rajendran.pdf'
# file = 'files/Copy of Resume-Haripriya Rajendran.pdf'

create_embeddings(file)
index = pc.Index("my-portfolio")
print(index.describe_index_stats())