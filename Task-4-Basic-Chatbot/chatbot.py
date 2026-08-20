# CodeAlpha Internship - Task 4
# Basic Chatbot

print("Chatbot: Hello! I am a simple Python chatbot.")
print("Chatbot: You can say hello, ask how I am, ask my name, or say bye.")
print("Chatbot: Type 'bye' to end the conversation.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Chatbot: Hello! Nice to meet you.")

    elif "how are you" in user_input:
        print("Chatbot: I'm doing great! Thanks for asking.")

    elif "your name" in user_input or "who are you" in user_input:
        print("Chatbot: I'm a basic chatbot created using Python.")

    elif "help" in user_input:
        print("Chatbot: You can greet me, ask how I am, ask my name, or say bye.")

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand that yet.")
