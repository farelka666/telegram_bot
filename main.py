import os
import random 
import time
import telebot



bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start',])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет! Я бот мусорщик')




@bot.message_handler(commands=['help'])
def commands(message):
    bot.send_message(message.chat.id,'''/help-показывает команды
/start-активирует бота
/tabl-показывает таблицу с расписанием выкидования мусора         
/sort-показывает виды мусорных баков для переработки                    
                     
                     ''')


@bot.message_handler(commands=['sort',])
def send_welcome(message):
    bot.send_message(message.chat.id,'''пластик
    стекло
    железки
    деревяшки
    еда''')


@bot.message_handler(commands=['tabl'])
def send_mem(message):
    
    
    with open('tablica.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 









print('you bot started')
bot.polling()


