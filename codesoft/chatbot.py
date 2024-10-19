def chatbot():
    print("Hello! I'm your chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Predefined responses using if-else
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot!")
        
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather right now, but you can use a weather app.")
        
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but thank you for asking!")
        
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

# Start chatbot
chatbot()
