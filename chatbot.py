def respond_to_user(user_input):
    # Convert the input to lowercase to avoid case sensitivity issues
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you?"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    elif "python" in user_input:
        return "Python is a popular programming language for web development, automation, and data analysis."
    elif "weather" in user_input:
        return "I'm not able to check the weather right now, but I hope it's nice outside!"
    elif "your name" in user_input:
        return "I'm a chatbot. You can call me Chatbot."
    elif "help" in user_input:
        return "I can provide information about Python, the weather, and more. Just ask me!"
    elif "age" in user_input:
        return "I'm a computer program, so I don't have an age. But I was created in 2021."
    elif "thank you" in user_input:
        return "You're welcome! If you have any other questions, feel free to ask."
    elif "your creator" in user_input:
        return "I was created by a software developer named Raghunandan."
    elif "joke" in user_input:
        return "Why did the computer go to the doctor? Because it had a virus!"
    elif "favorite color" in user_input:
        return "I'm a chatbot, so I don't have a favorite color. But I like all colors!"
    elif "how are you" in user_input:
        return "I'm a computer program, so I don't have feelings, but I'm here to help you!"
    elif "what can you do" in user_input:
        return "I can provide information about Python, the weather, tell jokes, and more. Just ask me!"
    elif "what time" in user_input:
        return "I'm not able to check the time right now, but you can check the time on your device."
    else:
        return "I didn't quite understand that. Can you try asking something else?"

    

# Main loop to keep the conversation going
while True:
    # Get input from the user
    user_input = input("You: ")
    
    # If the user wants to exit the chat
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Get the chatbot's response
    response = respond_to_user(user_input)
    
    # Print the response
    print(f"Chatbot: {response}")
    
    

