import openai  # OpenAI API for AI responses
import tkinter as tk  # Tkinter for GUI
from tkinter import scrolledtext
import speech_recognition as sr  # Speech recognition for voice input
import pyttsx3  # Text-to-Speech output

# 🔹 Set your OpenAI API key
API_KEY = "your_openai_api_key_here"

# 🔹 Initialize Text-to-Speech engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 160)  # Set speech speed

def chat_with_gpt(prompt):
    """
    Sends user input to OpenAI's GPT-3.5 API and retrieves the chatbot's response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            api_key=API_KEY
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

def send_message():
    """
    Sends the user's message to OpenAI and displays the response in the chat window.
    """
    user_input = user_entry.get().strip()
    
    if not user_input:  # Ignore empty input
        return

    chat_box.insert(tk.END, f"\n👤 You: {user_input}\n")  # Display user message
    user_entry.delete(0, tk.END)  # Clear input field
    
    response = chat_with_gpt(user_input)  # Get AI-generated response
    chat_box.insert(tk.END, f"🤖 ChatBot: {response}\n")  # Display chatbot response
    chat_box.yview(tk.END)  # Auto-scroll to the latest message

    speak_response(response)  # Convert AI response to speech

def voice_input():
    """
    Uses speech recognition to capture user's voice input and send it to the chatbot.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        chat_box.insert(tk.END, "\n🎙️ Listening...\n")
        root.update()  # Update GUI while listening
        
        try:
            audio = recognizer.listen(mic, timeout=5)
            user_input = recognizer.recognize_google(audio).strip()
            chat_box.insert(tk.END, f"👤 You (Voice): {user_input}\n")
            chat_box.yview(tk.END)

            response = chat_with_gpt(user_input)  # Get AI response
            chat_box.insert(tk.END, f"🤖 ChatBot: {response}\n")
            chat_box.yview(tk.END)

            speak_response(response)  # Speak response

        except sr.UnknownValueError:
            chat_box.insert(tk.END, "❌ Could not understand. Please try again.\n")
        except sr.RequestError:
            chat_box.insert(tk.END, "❌ Speech recognition service error.\n")

def speak_response(response):
    """
    Converts chatbot response text to speech.
    """
    tts_engine.say(response)
    tts_engine.runAndWait()

# 🔹 Create GUI Window
root = tk.Tk()
root.title("Voice AI Chatbot 🤖🎙️")  # Window Title
root.geometry("500x550")  # Set window size

# 🔹 Chat History Display (Scrollable)
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_box.pack(padx=10, pady=10)

# 🔹 User Input Box
user_entry = tk.Entry(root, font=("Arial", 14), width=40)
user_entry.pack(pady=5)

# 🔹 Send Button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# 🔹 Voice Command Button
voice_button = tk.Button(root, text="🎙️ Speak", font=("Arial", 12), command=voice_input)
voice_button.pack(pady=5)

# 🔹 Run the GUI
root.mainloop()
