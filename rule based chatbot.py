import random

def simple_chatbot(input_message):
    # Define rules for the chatbot
    rules = {
        'hello': ['Hi there!', 'Hello!', 'Hey!'],
        'how are you': ['I am doing well, thank you!', 'I\'m just a bot, but thanks for asking!'],
        'bye': ['Goodbye!', 'See you later!', 'Have a great day!'],
        'weather': ['I\'m sorry, I don\'t know the current weather.', 'You might want to check a weather website.'],
        'age': ['I don\'t have an age. I\'m just a computer program.', 'Age is just a number for me.'],
        'default': ["I'm sorry, I don't understand that. Can you please rephrase or ask something else?"]
    }

    # Convert the input message to lowercase for case-insensitive matching
    input_message_lower = input_message.lower()

    # Check if the input message matches any of the rules
    for pattern, responses in rules.items():
        if pattern in input_message_lower:
            return random.choice(responses)

    # If no match is found, use the default response
    return random.choice(rules['default'])

# Simple loop to keep the chatbot running
print("Chatbot: Hello! I'm a simple rule-based chatbot. You can say 'bye' to exit.")
while True:
    user_input = input("You: ")
    
    # Exit the loop if the user says 'bye'
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    
    # Get the chatbot's response based on user input
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
