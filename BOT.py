from telebot import TeleBot

BOT_TOKEN = 'MINHA CHAVE API'
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'olá'])
def send_welcome(message):
    bot.reply_to(message,'Olá, eu sou o Macoronosoraô!')

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()    