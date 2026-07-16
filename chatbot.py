# Simple Python Chatbot

print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("🤖 ChatBot: Hello! How are you?")

    elif user == "how are you":
        print("🤖 ChatBot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("🤖 ChatBot: My name is Python Bot.")

    elif user == "who created you":
        print("🤖 ChatBot: I was created using Python.")

    elif user == "what can you do":
        print("🤖 ChatBot: I can answer simple questions and chat with you.")

    elif user == "time":
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"🤖 ChatBot: The current time is {current_time}")

    elif user == "date":
        from datetime import datetime
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"🤖 ChatBot: Today's date is {current_date}")

    elif user == "bye":
        print("🤖 ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand that.")
