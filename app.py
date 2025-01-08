import time
from PyPDF2 import PdfReader
import streamlit as st
import google.generativeai as genai

# PDF Text Extraction
def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# AI Chat Function
genai.configure(api_key="AIzaSyBBF5wppFXSqZdP2Ffi2x08zMCwlgldeE4")

def chat_with_ai(pdf_text, user_input):
    try:
        relevant_text = pdf_text[:2000]
        prompt = f"Here is the relevant PDF content:\n{relevant_text}\n\nUser: {user_input}\nChatbot:"
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if hasattr(response, 'parts'):
            return [part.text for part in response.parts]
        else:
            return [response.text]
    except Exception as e:
        st.error(f"Error generating AI response: {e}")
        return ["Sorry, there was an issue generating the response."]

# Main Function
def main():
    st.title("Chat with PDF")
    uploaded_pdf = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_pdf and "pdf_text" not in st.session_state:
        st.session_state.pdf_text = extract_text_from_pdf(uploaded_pdf)

    pdf_text = st.session_state.get("pdf_text", "")

    if not pdf_text:
        st.write("Upload a PDF to start chatting!")
        return

    st.text_area("Extracted PDF Content", pdf_text, height=200, disabled=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # Display the conversation history
    for i, entry in enumerate(st.session_state.conversation):
        st.write(f"**You:** {entry['user']}")
        st.write(f"**Chatbot:** {entry['bot']}")

    # Query input: create a new input box for each query using the next query number.
    query_key = len(st.session_state.conversation)

    new_query = st.text_input(f"Your query {query_key + 1}:", key=f"query_{query_key}")

    # On Submit
    if st.button("Submit", key=f"submit_{query_key}"):
        if new_query.lower() == "exit":
            st.write("Chatbot: The conversation has ended.")
        elif new_query.strip():
            # Start timing
            start_time = time.time()

            # Get AI response
            ai_response = chat_with_ai(pdf_text, new_query)

            # Measure elapsed time
            elapsed_time = time.time() - start_time

            # Update conversation in session state
            st.session_state.conversation.append({
                "user": new_query,
                "bot": "\n".join(ai_response)
            })

            # Display response time
            st.write(f"AI response time: {elapsed_time:.2f} seconds")

            # Display the latest response immediately
            st.write(f"**You:** {new_query}")
            st.write(f"**Chatbot:** {st.session_state.conversation[-1]['bot']}")

if __name__ == "__main__":
    main()
