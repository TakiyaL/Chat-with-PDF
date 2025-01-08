from PyPDF2 import PdfReader
import streamlit as st
import google.generativeai as genai
import time

@st.cache_data
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None


def chunk_text(text, chunk_size=500):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

genai.configure(api_key="AIzaSyBBF5wppFXSqZdP2Ffi2x08zMCwlgldeE4")

def chat_with_ai(pdf_text, user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Here is the content of the PDF:\n{pdf_text}\n\nUser: {user_input}\nChatbot:"
        response = model.generate_content(prompt)

        if hasattr(response, 'parts'):
            return [part.text for part in response.parts]
        else:
            return [response.text] 
    except Exception as e:
        st.error(f"Error with AI response: {e}")
        return ["Sorry, there was an issue generating the response."]

def main():
    st.title("Chat with PDF")
    st.write(
        """
        Upload a PDF file and ask questions based on its content.
        The AI will respond based on the PDF contents.
        Type 'exit' to end the conversation.
        """
    )
    
    # State variables for conversation
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    if "query_count" not in st.session_state:
        st.session_state.query_count = 0 
    
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

        # Chat interaction
        st.subheader("Chat")
        
        # Debugging: Check the structure of the conversation
        if st.session_state.conversation:
            for i, entry in enumerate(st.session_state.conversation):
                if "user" in entry and "bot" in entry:
                    st.write(f"**You:** {entry['user']}")
                    st.write(f"**Chatbot:** {entry['bot']}")
                else:
                    st.error(f"Conversation entry at index {i} is invalid: {entry}")

        # Input for the next query
        new_query = st.text_input("Ask your question:", key=f"query_{st.session_state.query_count}")
        
        if st.button("Submit"):
            if new_query:
                if new_query.lower() == "exit":
                    st.write("Chatbot: The conversation has ended.")
            else:
                start_time = time.time()
                # Get AI response
                ai_response = chat_with_ai(pdf_text, new_query)

                # Append the conversation to the history
                st.session_state.conversation.append({
                    "user": new_query,
                    "bot": "\n".join(ai_response)
                })

                # Increment the query count to generate a new input box
                st.session_state.query_count += 1

                st.write(f"AI response time: {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
