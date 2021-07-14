# function to create the chatbot
def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(name=name,
                  read_only=False,
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  storage_adapter="chatterbot.storage.SQLStorageAdapter")
    return Bot


# function to train the bot with a variety of topics
def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")


# function to train the bot with custom data
def custom_train(Bot, conversation):
    from chatterbot.trainers import ListTrainer
    trainer = ListTrainer(Bot)
    trainer.train(conversation)


# function to start and take responses from the chatbot
def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am RobotFriend. How can I help you")
    bye_list = ["bye friend", "bye", "good bye"]

    while (True):
        user_input = input("me: ")
        if user_input.lower() in bye_list:
            print("RobotFriend: Good bye and have a blessed day!")
            break

        response = Bot.get_response(user_input)
        print("RobotFriend:", response)


# create chatbot
home_bot = create_bot('RobotFriend')

# train all data
train_all_data(home_bot)

# check identity
identity = input("State your identity please: ")

# rules for responding to different identities
if identity == "Denada":
    print("Welcome, Denada. Happy to have you at home.")

elif identity == "Jane":
    print("Denada is out right now, but you are welcome to the house.")

else:
    print("Your access is denied here.")
    exit()

# custom data
house_owner = [
    "Who is the owner of this house?",
    "Denada is the owner of this house."
]
custom_train(home_bot, house_owner)

print("------ Training custom data ------")

if identity == 'Denada':
    city_born = [
        "Where was I born?",
        "Denada, you were born in Tirane."
    ]

    fav_book = [
        "What is my favourite book?",
        "That is easy. Your favourite book is A Little Life."
    ]

    fav_movie = [
        "What is my favourite movie?",
        "You have watched Interstellar more times than I can count."
    ]

    fav_sports = [
        "What is my favourite sport?",
        "You don't enjoy sports that much."
    ]
    # train chatbot with custom data
    custom_train(home_bot, city_born)
    custom_train(home_bot, fav_book)
    custom_train(home_bot, fav_movie)
    custom_train(home_bot, fav_sports)

# start chatbot
start_chatbot(home_bot)