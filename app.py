from PyPDF2 import PdfReader
import streamlit as st
import google.generativeai as genai

def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None


def chunk_text(text, chunk_size=500):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

genai.configure(api_key="AIzaSyBBF5wppFXSqZdP2Ffi2x08zMCwlgldeE4")

def chat_with_ai(pdf_text, user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Here is the content of the PDF:\n{pdf_text}\n\nUser: {user_input}\nChatbot:")

    if hasattr(response, 'parts'):
        return [part.text for part in response.parts]
    else:
        return [response.text] 


def main():
    st.title("Chat with PDF")
    st.write(
        """
        Upload a PDF file and ask questions based on its content.
        The AI will respond based on the PDF contents.
        Type 'exit' to end the conversation.
        """
    )

    # Upload PDF file
    uploaded_pdf = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_pdf is not None:
        # Extract text from PDF
        pdf_text = extract_text_from_pdf(uploaded_pdf)

        if not pdf_text:
            return

        # Display the extracted PDF text (optional, for debugging or understanding content)
        st.subheader("Extracted Text from PDF:")
        st.text_area("PDF Content", pdf_text, height=200)

         # Start a chat interaction
        user_input = st.text_input("You: ", "")

        if user_input.lower() == "exit":
            st.write("Chatbot: The conversation has ended.")
            return

        if user_input:
            # Get the AI's response
            ai_response = chat_with_ai(pdf_text, user_input)

            # Display the AI's response
            for part in ai_response:
                st.write(f"Chatbot: {part}")

            # Clear the input field after user submits the question
            st.text_input("You: ", value="", key="clear_input")

if __name__ == "__main__":
    main()
