from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Load FAISS vectorstore and embedding model
faiss_store = FAISS.load_local("faiss_store", HuggingFaceEmbeddings("all-MiniLM-L6-v2"))
llm = OpenAI(temperature=0.7)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=faiss_store.as_retriever())

while True:
    query = input("Enter your query (type 'exit' to quit): ")
    if query.lower() == "exit":
        break
    answer = qa_chain.run(query)
    print(f"Answer: {answer}")
