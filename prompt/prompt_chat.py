from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

# to run this file use -> streamlit run .\prompt_chat.py

st.header("HuggingFace Chat Model Test")

user_input = st.text_input("Enter your question:")

if st.button("Submit"):
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task="text-generation"
    )

    model = ChatHuggingFace(llm=llm)

    response = model.invoke(user_input)

    st.write("Response:")
    st.write(response.content)