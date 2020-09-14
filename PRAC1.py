import telepot


token='1194605596:AAGUUDPGVtOrMMFdIcx3Esk_gQMotPwmQ7Q'
bot = telepot.Bot(token)
print (bot.getMe())

    
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))
bot.message_loop(handle)
