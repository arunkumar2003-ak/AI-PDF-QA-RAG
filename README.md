# 📄 AI PDF Question Answering System (RAG)

An AI-powered PDF Question Answering System built using **Python, Streamlit, LangChain, FAISS, and Google Gemini**. The application allows users to upload PDF documents and ask questions about their content. It uses a **Retrieval-Augmented Generation (RAG)** pipeline to retrieve the most relevant document sections before generating accurate answers.

---

## 🚀 Features

* Upload PDF documents
* Extract text from PDF files
* Split documents into smaller chunks using LangChain
* Generate embeddings for semantic search
* Store embeddings in FAISS Vector Database
* Retrieve relevant document chunks using similarity search
* Generate accurate answers using Google Gemini
* Interactive Streamlit web interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* Google Gemini API
* PyPDF
* HuggingFace Embeddings

---

## 📂 Project Structure

```text
AI_PDF_QA_RAG/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
|__.gitignore
|___Output.png


```

## 📌 How It Works

1. Upload a PDF document.
2. Extract text using PyPDF.
3. Split text into chunks with LangChain.
4. Generate embeddings and store them in FAISS.
5. Retrieve the most relevant chunks using semantic search.
6. Pass the retrieved context to Google Gemini.
7. Display accurate answers based on the uploaded PDF.

---

## 🔮 Future Enhancements

* Support multiple PDF uploads
* Chat history and conversation memory
* Display source page numbers
* Export chat history
* User authentication

---


###home_image 
![Home Page](home.png)

### PDF Upload
![PDF Upload](upload.png)

### Generated Answer
![Generated Answer](output.png)




## 👨‍💻 Author

Arun Kumar T

If you found this project useful, feel free to ⭐ the repository.
