# import telebot
# import time

# bot = telebot.TeleBot("5874489053:AAFZ8uGXWJhVXy0zcEbWKjV0N_HiSuI1AaI")
# mesage = ['Hello']
# @bot.message_handler(commands =['start'])
# def start(message):
#     # with open('chatids.txt','a+')as chatids:
#     #     print(, file=chatids)
#     print(message.chat.id)
#     with open('chatids.txt', 'a+') as chatids:
#         print(message.chat.id, file=chatids)
#     mess = f'Hello, <b>{message.from_user.first_name}</b>'
#     bot.send_message(message.chat.id,mess, parse_mode='html')
#     sent = bot.reply_to(message, 'Write something...')


# @bot.message_handler(commands=['rasylka'])
# def rassylka(message):
#     if message.chat.id == 1219398579:
#         for i in open('chatids.txt', 'r').readlines():
#             bot.send_message(i,"Hi everyone, how ar you?")


# @bot.message_handler(commands =['help'])
# def help(message):
#     mes = f'wats happened <b>{message.from_user.first_name}</b>'
#     bot.send_message(message.chat.id,mes,parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     with open('chat.txt', 'a+') as chat:
#         print(f'{message.from_user.first_name}:{message.text}', file=chat)
#     if message.text == 'Hello':
#         bot.send_message(message.chat.id, "Salam!", parse_mode='html')
#     elif message.text == 'hello':
#         bot.send_message(message.chat.id, 'Hi', parse_mode='html')
#     elif message.text == 'Photo':
#         photo = open('icon.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == 'photo':
#         photo = open('icon.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     elif message.text == '😂':
#         bot.send_message(message.chat.id, 'Hii 😂😂')
#     elif message.text == '😁':
#         bot.send_message(message.chat.id, "😁😁😁😁😁")
#     # else:
#     #     bot.send_message(message.chat.id, "I'm not undertanding you!", parse_mode='html')

# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#    # bot.send_message(message.chat.id, 'Vau cool!', parse_mode='html')
#    time.sleep(2)
#    bot.send_message(message.chat.id, 'Wtf', parse_mode='html')
#    time.sleep(10)
#    bot.send_message(message.chat.id, 'It was joke', parse_mode='html')


# # bot.send_message(5527345895,'uydamisan?')

# bot.polling(none_stop=True)