from PyPDF2 import PdfReader

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

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")

def chat_with_ai(conversation_history):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("\n".join(conversation_history))

    if hasattr(response, 'parts'):
        return [part.text for part in response.parts]
    else:
        return [response.text] 


def main():
    pdf_path = input("Enter the path to your PDF: ").strip()
    pdf_text = extract_text_from_pdf(pdf_path)
    
    if not pdf_text:
        print("Failed to extract text from the PDF. Please check the file path and try again.")
        return
    
    conversation_history = [f"Here is the content of the PDF: \n{pdf_text}\n\nYou can start asking questions based on the content."]
    
    print("\nChatbot: I have loaded the content from the PDF. You can ask me questions about it.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        conversation_history.append(f"You: {user_input}")
        
        ai_response = chat_with_ai(conversation_history)
        
        for part in ai_response:
            print(f"Chatbot: {part}")
            conversation_history.append(f"Chatbot: {part}")
    
if __name__ == "__main__":
    main()
