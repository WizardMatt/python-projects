import random

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm good! How about you?", "Doing great!", "I'm just a bot, but I'm fine!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "your name": ["I'm ChatBot!", "You can call me ChatBot!"],
    "weather": ["I can't check real-time weather, but it's always a good day to code!"],
    "default": ["I'm not sure about that. Can you ask something else?", "I don't understand that."]
}

def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day!")
            break
        
        response = responses.get(user_input, responses["default"])  # Get response or default message
        print(f"🤖 ChatBot: {random.choice(response)}")  # Randomly choose a response

# Run the chatbot
chatbot()
