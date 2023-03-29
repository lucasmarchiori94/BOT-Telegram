from telebot import TeleBot

BOT_TOKEN = '5718661133:AAFky_ov_UjVCSUbJuji75E0lOWQbb5Lvoo'
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'olá'])
def send_welcome(message):
    bot.reply_to(message,'Olá, eu sou o Macoronosoraô!')

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()    