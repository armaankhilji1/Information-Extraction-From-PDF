import streamlit as st
import os
from PyPDF2 import PdfReader

from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from typing_extensions import Concatenate


## Streamlit app UI
st.set_page_config(page_title="PDF Q&A", layout="wide")
st.title("PDF Question Answering System")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyAZ3SpuiTctSxan3vQA1jCoZYRnLuhqrm4"

## Used if statement to check whether the PDF is uploaded or not. If uploaded then only perform further task
if uploaded_file is not None:
    # Read PDF
    pdfreader = PdfReader(uploaded_file)
    raw_text = ""
    for i, page in enumerate(pdfreader.pages):
        content = page.extract_text()
        if content:
            raw_text += content

    # Split text into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=5000,
        chunk_overlap=500,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    # Embeddings + FAISS
    embeddings_model = HuggingFaceEmbeddings(model_name="multi-qa-mpnet-base-dot-v1")
    vectorstore = FAISS.from_texts(texts, embeddings_model)

    # Initialize Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    # User Query
    query = st.text_input("Ask a question from your PDF:")

    if query:
        # Retrieve relevant chunks using similaruty search operation
        docs = vectorstore.similarity_search(query, k=10)
        context = "\n".join([d.page_content for d in docs[:3]])

        # Gemini prompt
        messages = [
            SystemMessage(content="You are an assistant that answers based only on the provided document."
                                    "If the answer exists, copy the exact text from the document. "
                                    "Do not invent or summarize."),
            HumanMessage(content=f"Document context:\n{context}\n\nQuestion: {query}")
        ]

        # Stretched and refined answer from Gemini
        ai_msg = llm.invoke(messages)
        raw_answer = ai_msg.content

        # Remove extra spaces & empty lines
        structured_answer = "\n\n".join([line.strip() for line in raw_answer.splitlines() if line.strip()])

        # Display
        st.subheader("Relevant answer from PDF:")
        st.write(structured_answer)

        # Show retrieved chunks from PDF
        with st.expander("Retrieved PDF Chunks (Exact Text)"):
            for doc in docs:
                st.write(doc.page_content)
                st.markdown("---")
