import os

import streamlit as st

from dotenv import load_dotenv

from pypdf import PdfReader

import google.generativeai as genai

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS


# -----------------------------

# Load Environment Variables

# -----------------------------

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# -----------------------------

# Streamlit UI

# -----------------------------

st.set_page_config(

    page_title="AI PDF Question Answering",

    page_icon="📄"

)

st.title("📄 AI PDF Question Answering System")

st.write("Upload a PDF and ask questions about its content.")


uploaded_file = st.file_uploader(

    "Choose a PDF",

    type="pdf"

)


if uploaded_file:

    pdf_reader = PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        extracted = page.extract_text()

        if extracted:

            text += extracted

       # -----------------------------
    # Split Text into Chunks
    # -----------------------------

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    st.success(f"PDF Loaded Successfully ({len(chunks)} Chunks Created)")

    # -----------------------------
    # Create Embeddings
    # -----------------------------

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

    # -----------------------------
    # Create FAISS Vector Store
    # -----------------------------

    vector_store = FAISS.from_texts(
        chunks,
        embeddings
    )

    # -----------------------------
    # Ask Question
    # -----------------------------

    question = st.text_input(
        "Ask a question about the PDF"
    )

    if question:

        with st.spinner("Searching document..."):

            docs = vector_store.similarity_search(
                question,
                k=3
            )

            context = ""

            for doc in docs:
                context += doc.page_content + "\n\n"

            prompt = f"""
You are an AI assistant.

Answer ONLY from the given context.

If the answer is not present in the context, reply:

"I couldn't find the answer in the uploaded PDF."

Context:
{context}

Question:
{question}
"""

            response = model.generate_content(prompt)

            st.subheader("Answer")

            st.write(response.text)