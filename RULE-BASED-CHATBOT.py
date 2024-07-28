import random
import re

def chatbot(user_input):
    responses = {
        # General greetings
        "hello": ["Hello there!", "Hi!", "Greetings!"],
        "how are you": ["I'm doing well, thanks for asking!", "I'm okay.", "I'm feeling good."],
        "goodbye": ["Goodbye!", "See you later!", "Farewell!"],

        # Weather related
        "weather": ["The weather is beautiful today!", "It's a bit cloudy.", "I don't have access to real-time weather information."],

        # Jokes
        "tell me a joke": ["Why did the chicken cross the road? To get to the other side!", "What do you call a lazy kangaroo? A pouch potato."],

        # Default
        "default": ["I didn't quite understand that. Can you rephrase it?"]
    }

    # Basic pattern matching
    for key, value in responses.items():
        if key in user_input.lower():
            return random.choice(value)

    # More complex pattern matching using regular expressions
    if re.match(r"what's your name", user_input, re.IGNORECASE):
        return "My name is Chatbot."
    elif re.match(r"how old are you", user_input, re.IGNORECASE):
        return "I don't have an age, but I was created recently."

    # Handle more complex queries or specific domains here

    return random.choice(responses["default"])

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chatbot(user_input)
    print("Chatbot:", response)
