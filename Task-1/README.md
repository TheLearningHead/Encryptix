# Task 1:  CHATBOT WITH RULE-BASED RESPONSES 

## Overview

ChatBuddy is a simple rule-based chatbot built using Python. This task involves creating a chatbot that responds to user inputs based on predefined rules, using `if-else` statements or pattern matching techniques to identify user queries and provide appropriate responses. This project helps in understanding the basics of natural language processing (NLP) and conversation flow.

## Features

- Responds to greetings like "hi" and "hello".
- Answers inquiries about its identity.
- Provides the current time and date upon request.
- Tells jokes for entertainment.
- Gracefully exits the conversation when the user says "bye" or "goodbye".

## Setup

### Prerequisites

- Python 3 installed on your machine.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/TheLearningHead/Encryptix.git
    ```
2. Navigate to the Task1 directory:
    ```sh
    cd Encryptix/Task1
    ```

## Usage

To start ChatBuddy, run the script:
```sh
python chatbot.py
```

Example conversation:
```
Welcome to ChatBuddy! Type 'bye' to exit the conversation.

You: Hi
ChatBuddy: Hello! How can I assist you today?

You: What is your name?
ChatBuddy: I am ChatBuddy, your friendly assistant chatbot! How can I assist you?

You: Tell me a joke
ChatBuddy: Why don't scientists trust atoms? Because they make up everything!

You: Goodbye
ChatBuddy: Goodbye! Have a great day! Hope to see you soon!
```

## Code Explanation

### Main Components

1. `chatbot_response(query)`: Function containing predefined responses based on user queries using `if-else` statements.
2. `chat_with_bot()`: Main function to interact with the chatbot, continuously prompting the user for input and printing the chatbot's response.

### Functions

- `chatbot_response(query)`: This function handles the following queries:
  - Greetings: "hi", "hello"
  - Status check: "how are you"
  - Casual conversation: "what's up"
  - Identity: "what's your name", "who are you"
  - Time: "time"
  - Date: "today's date"
  - Jokes: "joke"
  - Exit: "bye", "goodbye"
