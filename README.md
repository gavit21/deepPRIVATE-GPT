# PrivateGPT Chatbot

## Overview
PrivateGPT is a chatbot designed to answer questions based on your documents. It ensures privacy by processing everything locally.

## Features
- Document ingestion and vector storage using Weaviate.
- Retrieval-based Q&A with LangChain and HuggingFace.
- Simple frontend using Streamlit.
- Backend powered by FastAPI.

## Workflow
![ChatBot Workflow](https://github.com/gavit21/deepPRIVATE-GPT/blob/main/workflow_1.png)
![ChatBot Workflow](https://github.com/gavit21/deepPRIVATE-GPT/blob/main/chatbot.drawio(1).png)
![ChatBot Workflow](https://github.com/gavit21/deepPRIVATE-GPT/blob/chatbot.drawio(2).png)
## Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/your_username/privateGPT.git
cd privateGPT
```
2. Install Dependencies
```bash
conda create -n privategpt_env python=3.10 -y
conda activate privategpt_env
pip install -r requirements.txt
```
3. Prepare and process Documents 
Place your .pdf and .txt documents in the *source_documents/* directory. Then run:
```bash
python ingest.py
```
 This creates a local FAISS vectorstore for your documents.

4. Rub Chatbot
Start the chatbot by running:
```bash
python app.py
```
5. Use the Web Interface
Run the Streamlit UI:
```bash
streamlit run app_ui.py
```
Open the displayed URL in your browser to interact with the chatbot.