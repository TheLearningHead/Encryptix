import random
import datetime


# Function containing the predefined responses to queries
def chatbot_response(query):
    query = query.lower()

    if "hi" in query or "hello" in query:
        responses = ["Hello! How can I assist you today?", "Hi there! How can I help you?", "Hey! What's on your mind?"]
        return random.choice(responses)

    elif "how are you" in query:
        return "I am just a bot who is here to help you. Is there anything I can help you with?"

    elif "what's up" in query:
        return "Nothing much, just here to assist you."

    elif "what's your name" in query or "what is your name" in query or "who are you" in query:
        return "I am ChatBuddy, your friendly assistant chatbot! How can I assist you?"

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"

    elif "today's date" in query:
        date_today = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"The current time is {date_today}"

    elif "joke" in query:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!",
                 "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                 "I told my wife she should embrace her mistakes. She gave me a hug.",
                 "I'm reading a book on anti-gravity. It's impossible to put down!",
                 "Why did the scarecrow win an award? Because he was outstanding in his field!"]
        return random.choice(jokes)

    elif "bye" in query or "goodbye" in query:
        return "Goodbye! Have a great day! Hope to see you soon!"


# Main function to interact with the chatbot
def chat_with_bot():
    print("Welcome to ChatBuddy! Type 'bye' to exit the conversation.\n")
    while True:
        query = input("You: ")
        response = chatbot_response(query)
        if "goodbye" in response.lower():
            print(f"ChatBuddy: {response}")
            break
        print(f"ChatBuddy: {response}\n")


if __name__ == "__main__":
    chat_with_bot()
