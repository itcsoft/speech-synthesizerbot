import telebot 
import gtts
import datetime
import os
from telebot import types

current_path = os.path.abspath(os.getcwd())
token = '2079897959:AAFyEZgpuNyQl_j0X5IN2K943Vt56cEuvgU'

my_bot = telebot.TeleBot(token)
@my_bot.message_handler(commands=['start', 'старт'])
def say_hello(message):
    my_bot.send_message(message.chat.id, 'Hi, I am speech synthesizer!')



@my_bot.message_handler(commands=['alphabet'])
def alphabet(message):
    markup = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton('A')
    buttonB = types.KeyboardButton('B')
    buttonC = types.KeyboardButton('C')
    buttonD = types.KeyboardButton('D')
    buttonD = types.KeyboardButton('D')

    markup.row(buttonA, buttonB, buttonC)
    markup.row(buttonD)
    my_bot.send_message(message.chat.id, 'working', reply_markup=markup)


@my_bot.message_handler(commands=['alphabet2'])
def alphabet2(message):
    markup2 = types.InlineKeyboardMarkup()
    buttonA = types.InlineKeyboardButton('A', callback_data='a')
    buttonB = types.InlineKeyboardButton('B', callback_data='b')
    buttonC = types.InlineKeyboardButton('C', callback_data='c')
    buttonD = types.InlineKeyboardButton('d', callback_data='d')

    markup2.row(buttonA, buttonB, buttonC)
    markup2.row(buttonD)
    my_bot.send_message(message.chat.id, 'working', reply_markup=markup2)


@my_bot.message_handler(content_types='text')
def say_any(message):
    audio_name = datetime.datetime.now()
    text = message.text
    say = gtts.gTTS(text, lang='en', slow=False)
    say.save(f'{audio_name}.mp3')
    final_path = f'{current_path}/{audio_name}.mp3'
    audio_file = open(final_path, 'rb')
    my_bot.send_audio(message.chat.id, audio_file)
    my_bot.send_message(message.chat.id, 'I have sended!')


print('Bot is working...')
my_bot.infinity_polling()
