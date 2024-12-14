print("Hello! I am your chatbot. Ask me something!")

responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm doing great, thank you for asking! How about you?",
    "your name": "I am a chatbot, here to help you!",
    "bye": "Goodbye! Have a great day!",
    "what can you do": "I can chat with you, tell jokes, share facts, or help with simple queries!",
    "joke": "Why don't skeletons fight each other? They don't have the guts!",
    "fact": "Did you know? The Eiffel Tower can be 15 cm taller during hot days due to metal expansion.",
    "hobby": "My hobby is chatting with people like you!",
}

while True:
    user_input = input("You: ")

    if user_input == "hello":
        print("Chatbot:", responses["hello"])
    elif user_input == "how are you":
        print("Chatbot:", responses["how are you"])
    elif user_input == "your name":
        print("Chatbot:", responses["your name"])
    elif user_input == "what can you do":
        print("Chatbot:", responses["what can you do"])
    elif user_input == "joke":
        print("Chatbot:", responses["joke"])
    elif user_input == "fact":
        print("Chatbot:", responses["fact"])
    elif user_input == "hobby":
        print("Chatbot:", responses["hobby"])
    elif user_input == "bye":
        print("Chatbot:", responses["bye"])
        break
    else:
        print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")



