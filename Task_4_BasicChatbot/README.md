# CodeAlpha Basic Chatbot

A simple rule-based command line chatbot written in Python. It normalizes the
user's input and selects a predefined response for supported phrases.

## Features

- Responds to greetings and questions such as “How are you?”
- Answers identity questions about the bot and who created it.
- Responds to thanks and statements like “I am fine.”
- Shows a fallback message when it does not recognize an input.
- Ends the chat when the user enters `bye`, `goodbye`, `exit`, or `quit`.
- Ignores blank input and handles Ctrl+C or end-of-input gracefully.

## Requirements

- Python 3
- No third-party packages; the script uses Python's standard library.

## Run

Open a terminal in the folder containing `basic_chatbot.py` and run:

```bash
python basic_chatbot.py
```

On some systems, use `python3` instead:

```bash
python3 basic_chatbot.py
```

## Example

```text
You: Hello!
Bot: Hello! How can I help you today?

You: Who created you?
Bot: Wendy, a Computer engineering student

You: bye
Bot: Goodbye! Have a great day!
```

The chatbot uses phrase matching rather than an AI model, so it only responds
to the patterns defined in `basic_chatbot.py`code.


##  Repository Structure
```text
Task_4_BasicChatbot/
├── basic_chatbot.py      # Main script
└── README.md            # Project documentation
```

---