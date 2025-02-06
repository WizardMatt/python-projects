import openai  # Import OpenAI for API calls
import tkinter as tk  # Import Tkinter for GUI
from tkinter import scrolledtext

# 🔹 Set your OpenAI API key (Replace "your_openai_api_key_here" with your actual key)
API_KEY = "your_openai_api_key_here"

def chat_with_gpt(prompt):
    """
    Sends user input to OpenAI's GPT-3.5 API and retrieves the chatbot's response.

    Parameters:
    - prompt (str): The user's message.

    Returns:
    - str: The chatbot's response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            api_key=API_KEY
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"  # Handle errors gracefully

def send_message():
    """
    Sends the user's message to OpenAI and displays the response in the chat window.
    """
    user_input = user_entry.get()  # Get text from input box
    
    if user_input.strip() == "":  # Ignore empty inputs
        return

    chat_box.insert(tk.END, f"\n👤 You: {user_input}\n")  # Display user message
    user_entry.delete(0, tk.END)  # Clear input field
    
    response = chat_with_gpt(user_input)  # Get AI-generated response
    chat_box.insert(tk.END, f"🤖 ChatBot: {response}\n")  # Display chatbot response
    chat_box.yview(tk.END)  # Auto-scroll to the latest message

# 🔹 Create GUI Window
root = tk.Tk()
root.title("AI Chatbot 🤖")  # Window Title
root.geometry("500x500")  # Set window size

# 🔹 Chat History Display (Scrollable)
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_box.pack(padx=10, pady=10)

# 🔹 User Input Box
user_entry = tk.Entry(root, font=("Arial", 14), width=40)
user_entry.pack(pady=5)

# 🔹 Send Button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# 🔹 Run the GUI
root.mainloop()
