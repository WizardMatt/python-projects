import openai  # Import OpenAI module for API access

# 🔹 Set your OpenAI API key (Replace "your_openai_api_key_here" with an actual key)
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
        response = openai.ChatCompletion.create(  # Make a request to OpenAI API
            model="gpt-3.5-turbo",  # Using the GPT-3.5 Turbo model
            messages=[{"role": "user", "content": prompt}],  # Sending user input
            api_key=API_KEY  # Providing API key for authentication
        )
        
        # Extracting and returning the chatbot's response
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Error: {str(e)}"  # Handle errors gracefully

# 🔹 Start a conversation loop
print("🤖 AI ChatBot: Hello! Type 'exit' to stop.")

while True:
    user_input = input("You: ")  # Get user input
    
    if user_input.lower() == "exit":  # Check if the user wants to exit
        print("🤖 AI ChatBot: Goodbye! Have a great day! 🚀")
        break  # Exit the loop
    
    response = chat_with_gpt(user_input)  # Get AI-generated response
    print(f"🤖 AI ChatBot: {response}")  # Display the chatbot's response
