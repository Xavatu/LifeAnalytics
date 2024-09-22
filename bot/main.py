import datetime
import telebot

from bot.config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    print(message.from_user.__dict__)
    username = message.from_user.username
    response_text = "pong"
    print(f"\n{datetime.datetime.now()}\t@{username}:\t{message.text}")
    bot.send_message(chat_id=message.from_user.id, text=response_text)


bot.polling()
