---------------------------------------------------------------
TASK : 3 
CODE ALPHA INTERSHIP : BASIC CHATBOT

----------------------------------------------------------------




import datetime
import random
import re

RESPONSES = {
    "greetings": [
        "Hey! How's it going?",
        "Hello! How can I help you today?",
        "Hi! Good to see you."
    ],
    "wellbeing": [
        "I'm doing well, thanks for asking! How about you?",
        "All good here! Hope you're having a productive day.",
        "Doing great! What's on your mind?"
    ],
    "identity": [
        "I'm AlphaBot, a basic rule-based console bot.",
        "Just a lightweight Python chatbot running in your terminal."
    ],
    "farewell": [
        "Bye! Have a nice day.",
        "See you later!",
        "Goodbye! Take care."
    ],
    "fallback": [
        "Sorry, I didn't quite catch that. Type 'help' if you're stuck.",
        "I don't have an answer for that yet. Try asking something else.",
        "Could you rephrase that?"
    ]
}

def calculate(text):
    match = re.search(r"calc\s*([\d\+\-\*\/\s\.\(\)]+)", text)
    if match:
        try:
            return f"Answer: {eval(match.group(1), {'__builtins__': None}, {})}"
        except Exception:
            return "Invalid math expression."
    return None

def get_reply(user_msg):
    msg = user_msg.lower().strip()

    if msg in ["bye", "exit", "quit", "cya"]:
        return random.choice(RESPONSES["farewell"])

    calc_res = calculate(msg)
    if calc_res:
        return calc_res

    if "time" in msg:
        return f"Current time: {datetime.datetime.now().strftime('%I:%M %p')}"

    if "date" in msg or "day" in msg:
        return f"Today's date: {datetime.datetime.now().strftime('%A, %d %B %Y')}"

    if any(w in msg for w in ["hello", "hi", "hey", "sup"]):
        return random.choice(RESPONSES["greetings"])

    if any(w in msg for w in ["how are you", "how r u"]):
        return random.choice(RESPONSES["wellbeing"])

    if any(w in msg for w in ["who are you", "your name"]):
        return random.choice(RESPONSES["identity"])

    if "help" in msg:
        return "Commands: greetings, 'time', 'date', 'calc 10+5', or 'bye' to exit."

    return random.choice(RESPONSES["fallback"])

def main():
    print("=" * 45)
    print("       🤖 Console Chatbot (Task 4) 🤖")
    print("=" * 45)
    print("Type 'help' for options or 'bye' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            reply = get_reply(user_input)
            print(f"Bot: {reply}\n")

            if user_input.lower().strip() in ["bye", "exit", "quit", "cya"]:
                break
        except (KeyboardInterrupt, EOFError):
            print("\nSession ended. Bye!")
            break

if __name__ == "__main__":
    main()