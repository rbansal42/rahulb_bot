import requests as re
import telebot
import json
import os

Tele_API_KEY = os.getenv("Tele_API_KEY")
Tenor_API_KEY = os.getenv("Tenor_API_KEY")

bot = telebot.TeleBot(Tele_API_KEY)

chat_ID = {'jiya' : 1101727386, 'rahul': 940075808}

# This Command will send a URL that will serve the user with a dog Image/Gif
@bot.message_handler(commands=['woof', 'Woof', 'Dog', 'dog'])
def woof(message):

  contents = re.get('https://random.dog/woof.json').json()
  image_url = contents['url']
  bot.send_message(message.chat.id, "Woof! \n" + image_url)

# This Command will send a URL that will serve the user with a cat Image/G
@bot.message_handler(commands=['meow', 'cat', 'Meow', 'Cat'])
def meow(message):

  contents = re.get('https://cataas.com/cat?json=true').json()
  image_url = "https://cataas.com" + contents['url']
  bot.send_message(message.chat.id, "Meow! \n" + image_url)

# Starting the bot
@bot.message_handler(commands=['start','Start'])
def start(message):

  first_name = message.chat.first_name
  msg = "Hello " + first_name
  ID = "Your user ID is " + str(message.chat.id)
  
  bot.send_message(message.chat.id, msg)
  bot.send_message(message.chat.id, ID)

# The command to send GIFs
@bot.message_handler(commands=['gif', 'Gif'])
def gif(message):
    base_url = "https://g.tenor.com/v1/random?" 

    with open('pos.json') as db:
      next = json.load(db)

    key = '&key=' + Tenor_API_KEY
    q = '&q=' + 'funny'
    media_filter = '&media_filter=minimal'
    limit = '&limit=5'
    pos = '&pos=' + str(next["pos"])    

    json_url = base_url + q + key + media_filter + limit + pos
    print(json_url)
    contents = re.get(json_url).json()

    # bot.send_message(chat_ID['rahul'], "Rahul wants me to remind you that he loafs you ")

    for x in range(2):
        gif_URL = contents['results'][x]['media'][0]['gif']['url']
        bot.reply_to(message, gif_URL)


    next_pos = {'pos' : contents["next"]}
    os.remove("pos.json")
    with open("pos.json", 'w') as db:
      json.dump(next_pos, db)
    


bot.polling()