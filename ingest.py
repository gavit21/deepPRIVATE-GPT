import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def process_documents(source_dir, embeddings_model_name):
    loaders = {
        ".pdf": PyPDFLoader,
        ".txt": TextLoader
    }
    documents = []
    for root, _, files in os.walk(source_dir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in loaders:
                loader = loaders[ext](os.path.join(root, file))
                documents.extend(loader.load())

    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # Create embeddings and FAISS vectorstore
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save the vectorstore to disk
    vectorstore.save_local("faiss_store")

if __name__ == "__main__":
    process_documents("source_documents", "all-MiniLM-L6-v2")
