import nltk
from nltk.chat.util import Chat, reflections

# Pairs of input and responses
pairs = [
    ["hi|hello|hey", ["Hello! How can I help you?"]],
    ["what is your name?", ["I'm CodTechBot, your AI assistant."]],
    ["how are you?", ["I'm just a bunch of code, but I'm doing fine!"]],
    ["(.*) your name?", ["My name is CodTechBot."]],
    ["quit", ["Bye! Take care."]],
    ["(.*)", ["Sorry, I didn't get that. Can you rephrase?"]]
]

def main():
    print("Hi! I'm CodTechBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    main()
