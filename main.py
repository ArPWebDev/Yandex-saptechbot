import telebot
TOKEN = '5288724500:AAEmdKOa1GKnX-eq0l0dig04xndMLWBSZk8'



bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text']) 
def message_handler(message):
    bot.send_message(message.chat.id, message.text) 

bot.polling(non_stop=True)
