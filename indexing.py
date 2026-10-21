import os
import json
import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader,PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def build_store():

    loader = PyPDFDirectoryLoader(path='./content/agentic_ai_research_papers/')
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name='cl100k_base',
        chunk_size=1000,
        chunk_overlap=200
    )
    
    research_paper_chunks = loader.load_and_split(text_splitter)

    embedding_model = OpenAIEmbeddings(model='text-embedding-ada-002')
    vectorestore = Chroma.from_documents(
        research_paper_chunks,
        embedding_model,
        collection_name='research_papers'
    )

    return vectorestore

