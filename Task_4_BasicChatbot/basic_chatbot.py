import re

def get_response(user_input: str) -> str:
    """
    Processes user input and returns a predefined response based on rule matching.
    """
    # Clean and normalize input (`lowercase & remove surrounding whitespace)
    cleaned_input = user_input.lower().strip()
    
    # Remove punctuation for better pattern matching
    normalized_input = re.sub(r'[^\w\s]', '', cleaned_input)

    # 1. Exit / Farewell Intents
    if any(word in normalized_input for word in ['bye', 'goodbye', 'exit', 'quit', 'see you']):
        return "Goodbye! Have a great day!"

    # 2. Greetings
    elif any(normalized_input.startswith(greet) or normalized_input == greet for greet in ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good evening', 'good afternoon']):
        return "Hello! How can I help you today?"

    # 3. Status Check
    elif 'how are you' in normalized_input or 'hows it going' in normalized_input or 'how do you do' in normalized_input:
        return "I'm doing well, thank you for asking! How are you doing today?"

    # 4. Identity / Name
    elif 'your name' in normalized_input or 'who are you' in normalized_input:
        return "I am CodeAlpha Bot, a simple rule-based chatbot written in Python!"

    # 5. Creator
    elif any(phrase in normalized_input for phrase in ['who created it', 'who created you', 'who made you', 'who is your creator']):
        return "Wendy, a Computer engineering student"

    # 6. Help
    elif 'what can you do' in normalized_input or 'help' in normalized_input or 'options' in normalized_input:
        return "I can answer basic questions, greet you, and chat! Try asking 'how are you', 'who are you', or say 'bye' to exit."

    # 7. Gratitude
    elif 'thank' in normalized_input or 'thanks' in normalized_input:
        return "You're very welcome! Let me know if you need anything else."
    

    # 8. User state response
    elif any(phrase in normalized_input for phrase in ['i am good', 'im good', 'i am fine', 'im fine', 'doing well', 'great']):
        return "Glad to hear that! How can I assist you further?"

    # 9. Default Response
    else:
        return "I'm sorry, I didn't quite understand that. Type 'help' to see what I can do, or say 'bye' to leave."


def run_chatbot():
    """
    Main loop for running the interactive terminal chatbot.
    """
    print("*" * 50)
    print("      Welcome to CodeAlpha Basic Chatbot!      ")
    print("  (Type 'bye', 'exit', or 'quit' to end chat)  ")
    print("*" * 50)
    print("Bot: Hi! I'm your assistant. How can I help you today?\n")

    while True:
        try:
            user_input = input("You: ")
            if not user_input.strip():
                continue

            response = get_response(user_input)
            print(f"Bot: {response}\n")

            # Check if user wants to exit
            cleaned = re.sub(r'[^\w\s]', '', user_input.lower().strip())
            if any(word in cleaned for word in ['bye', 'goodbye', 'exit', 'quit']):
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break


if __name__ == "__main__":
    run_chatbot()
