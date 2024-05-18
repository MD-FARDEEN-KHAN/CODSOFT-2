import random

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "hola"]
    farewells = ["bye", "goodbye", "see you later", "take care"]
    gratitude = ["thank you", "thanks", "appreciate it", "much obliged"]
    emotions = ["I'm feeling great!", "I'm doing fine, thank you!", "I'm alright, thanks for asking!"]
    jokes = ["Why was the math book sad? Because it had too many problems!", 
             "Why don't scientists trust atoms? Because they make up everything!",
             "What do you get when you cross a snowman and a vampire? Frostbite!"]
    
    if any(greeting in user_input for greeting in greetings):
        return random.choice(["Hello! How can I assist you today?", 
                              "Hi there! What can I do for you?"])
    elif any(farewell in user_input for farewell in farewells):
        return random.choice(["Goodbye! Have a great day!", 
                              "Farewell! Come back soon!"])
    elif any(word in user_input for word in gratitude):
        return random.choice(["You're welcome!", "No problem!", "Anytime!"])
    elif "how are you" in user_input:
        return random.choice(emotions)
    elif "joke" in user_input:
        return random.choice(jokes)
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()    