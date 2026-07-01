print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hi there!")
    elif user == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user == "how are you doing":
        print("Bot: I'm doing great, thanks for asking!")
    elif user == "can you help me":
        print("Bot:Of course! Tell me what you need help with - I'm here for you.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I'm sorry, I don't understand.")


