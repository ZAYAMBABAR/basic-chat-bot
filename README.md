#  Simple Python Chatbot

A beginner-friendly chatbot built using **Python**. This project runs in the terminal and responds to predefined user inputs using Python's `if`, `elif`, and `else` statements.

---

##  Features

- 👋 Greets the user
- 😊 Responds to basic conversations
- ⏰ Displays the current time
- 📅 Displays today's date
- 💬 Interactive command-line interface
- 🚪 Exit the chatbot by typing `bye`

---

## 🛠️ Technologies Used

- Python 3
- Built-in `datetime` module

---

## Project Structure

```
Simple-Python-Chatbot/
│
├── chatbot.py
└── README.md
```

---

##  How to Run



### 2. Open the project folder

```bash
cd simple-python-chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

---

## Example Conversation

```
ChatBot: Hello! Type 'bye' to exit.

You: hi
 ChatBot: Hello! How are you?

You: what is your name
ChatBot: My name is Python Bot.

You: time
ChatBot: The current time is 10:45:12

You: date
ChatBot: Today's date is 16-07-2026

You: bye
ChatBot: Goodbye! Have a nice day.
```

---

## How It Works

The chatbot continuously waits for user input using a `while True` loop. It compares the entered text with predefined commands using `if`, `elif`, and `else` statements and prints the appropriate response.

If the user enters **bye**, the chatbot ends the conversation and exits the program.

---

## 📚 Concepts Practiced

- Variables
- User Input (`input()`)
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`while`)
- String Methods (`lower()`)
- Importing Modules
- Date and Time using `datetime`

---

##  Future Improvements

- Add more questions and responses
- Use dictionaries instead of multiple `if` statements
- Store chat history
- Build a graphical user interface (GUI)
- Integrate an AI API (OpenAI or Groq)
- Connect the chatbot with a database

---


