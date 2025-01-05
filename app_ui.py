import requests
import streamlit as st

st.title("PrivateGPT Chatbot")

question = st.text_input("Ask a question about your documents:")

if st.button("Submit"):
    response = requests.post("http://localhost:8000/query/", json={"question": question})
    if response.status_code == 200:
        st.write(f"Answer: {response.json()['answer']}")
    else:
        st.error("Error querying the chatbot.")
