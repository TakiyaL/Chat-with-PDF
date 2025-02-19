# Chat with PDF App

## Overview

The **Chat with PDF** app allows users to upload PDF files and interact with their content using a chatbot powered by Google's **Generative AI** model. You can ask questions based on the content of the PDF, and the AI will provide context-aware responses. This app is built using **Streamlit**, **PyPDF2**, and **Google Generative AI**.

## Features

- Upload a PDF file to the app.
- Automatically extracts the text from the uploaded PDF.
- Chat with the AI model based on the extracted PDF content.
- AI generates contextual responses to your questions.

## Technologies Used

- **Streamlit**: For creating the web interface.
- **PyPDF2**: For extracting text from PDF files.
- **Google Generative AI**: For generating chatbot-like responses.

## Setup Instructions

To run this app locally, follow these steps:

## Prerequisites

- Python 3.x installed on your system.
- A **Google API key** for **Google Generative AI**.
- A **GitHub account** for deploying the app on **Streamlit Cloud** (optional).

### Setup
```bash
# Clone the repository
git clone https://github.com/TakiyaL/chat-with-pdf.git
cd chat-with-pdf

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py

