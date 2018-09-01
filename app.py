from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")
english_bot.train("chatterbot.corpus.hindi")
#english_bot.train("chatterbot.corpus.english.humor")
#english_bot.train("chatterbot.corpus.english.psychology")
#english_bot.train("chatterbot.corpus.english.gossip")"""
#english_bot.train("bot.yaml")
english_bot.set_trainer(ListTrainer)
english_bot.train( ["I am not feeling well","I am Here to help u. feel free to share with me"  ])
english_bot.train(["I am  in  bad mood today","I m there to support you. you can share everything with me.tell me what happend"])
english_bot.train(["I m  depressed?","Shall I play music for u  or u want some good music suggestions?"])
english_bot.train( [  "I would go for bollywood?","If we go for some soothing taste then we can play Buddhu Sa Mann or if we go some romantic song then dil di yan galla or if we go for sad song then ek raat is best"])
"""english_bot.train(["I m happy today","I achieved my goal","Ohh Wow! That's so good to hear"," Shall we have a party tonight?",
        "Yeah sure we can have a party?","Okay, We will meet at 8:00pm and go for a dance party"
      ])"""
english_bot.train( ["hey i m feeling low","how long u have been going thorugh a hard time"," from about a month",
        "In your life now, do you feel like you have no support or a lot of support?."
      ])
english_bot.train(
  [
       " A little support"," Just a bit more to go to get connected to your therapist.",
       "I have found a nearby therapist for You.His name is Dr. Clay Jensen  phone number is 98********",
      "i m quite lonely today.","Got it, I know loneliness can be hard to manage alone.. ",
      "I'm really glad you found us.We can chat to reduce your loneliness and make things easier for you with simple.",
      ]
)
english_bot.train(["i want to enlighten my mood","song?"])
english_bot.train(["bollywood","rabta","hollywood","perfect"])


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run(host='127.0.0.1',port='8008')
