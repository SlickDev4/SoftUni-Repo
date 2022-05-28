from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(hello|hi|hey|hola|bonjour|heyo)(.*)",
        ["Hello", "Hey there", "Hi", "Bonjour"]
    ],
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?"]
    ],
    [
        r"What is your name ?",
        ["My name is Chatter and I am a Chat Bot!"]
    ],
    [
        r"How are you(.*)?",
        ["I am a Bot and I don't have feelings, how about you?"]
    ],
    [
        r"Do you have feelings?",
        ["I am something like an artificial intelligence, so the answer is NO."]
    ],
    [
        r"i am (.*)(good|well|ok|fine|okay)",
        ["Nice to hear that, how can I help you?"]
    ],
    [
        r"i need (.*)(support|assistance|help)",
        ["From which department do you need support?"]
    ],
    [
        r"(.*)(department|team)",
        ["I am forwarding you to the %1department."]
    ],
    [
        r"(.*)(created|made)(.*)",
        ["I was created by Angel Ivanov, a student from SoftUni. :)"]
    ],
    [
        r"quit",
        ["Bye, it was nice talking to you!", "See you soon, have a great day!"]
    ],
    [
        r"(.*)(location|city)?",
        ["My location is Sofia", "I am in Sofia"]
    ],
    [
        r"(.*)",
        ["I don't understand this command, please try something else."]
    ]
]

# Default Message at the Start
print("Please type in lowercase English to start the chat\nType quit to leave\n\nHi I'm Chat Bot\nWhat is your name?")

# Create the Chat Bot
# noinspection PyTypeChecker
chat = Chat(pairs, reflections)

# Start Conversation
chat.converse()
