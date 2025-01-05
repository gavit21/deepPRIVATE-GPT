from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from transformers import pipeline
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI()

# Initialize FAISS vectorstore and embeddings
faiss_store = FAISS.load_local("faiss_store", HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))

# Load Hugging Face transformer model
qa_pipeline = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B", tokenizer="EleutherAI/gpt-neo-2.7B")

# RetrievalQA chain
class Query(BaseModel):
    question: str

@app.post("/query/")
async def query(question: Query):
    if not question.question.strip():
        raise HTTPException(status_code=400, detail="Empty question provided.")
    
    # Retrieve documents
    retrieved_docs = faiss_store.similarity_search(question.question)
    context = " ".join([doc.page_content for doc in retrieved_docs])

    # Generate answer using the Hugging Face model
    input_text = f"Context: {context}\nQuestion: {question.question}\nAnswer:"
    result = qa_pipeline(input_text, max_length=256, num_return_sequences=1)
    answer = result[0]["generated_text"]
    
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
