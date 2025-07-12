def chatbot():
    print("Chatbot: Hello! Type something to chat. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "hi":
            print("Chatbot: Hello!")
        elif user_input == "how are you":
            print("Chatbot: I'm doing well, thank you!")
        elif user_input == "what's your name":
            print("Chatbot: I'm a simple chatbot.")
        elif user_input == "what can you do":
            print("Chatbot: I can chat with you and respond to some basic messages.")
        elif user_input == "thank you":
            print("Chatbot: You're welcome!")
        elif user_input == "thanks":
            print("Chatbot: No problem!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
