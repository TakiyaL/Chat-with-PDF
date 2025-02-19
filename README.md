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

##  Installation

  Steps to Install

  Clone the repository:

  git clone https://github.com/TakiyaL/Chat-with-PDF.git

  cd Chat-with-PDF


Install dependencies:

 ```bash
 pip install -r requirements.txt

Run the application:
 ```bash
 streamlit run app.py

##  Usage

Upload a PDF file.

The application will extract text from the document.

Enter a query in the chatbox to ask questions based on the uploaded PDF.

The AI will generate responses based on relevant PDF content.


## Future Enhancements

 Improved text extraction for complex PDFs (images, tables, etc.).

 Enhanced AI accuracy with better contextual understanding.

 More interactive UI features for better user experience.

 Support for multiple document formats (e.g., DOCX, TXT).



## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.
