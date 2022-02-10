from os import rename
import telebot
from telebot import types
from movieconfig import TOKEN
from service import sql
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text = 'Привет! Я ваш помощник по фильмам. Нажмите соответсвующую кнопку:'
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('выбрать фильм по категориям', callback_data='categories')
    btn2 = types.InlineKeyboardButton('ввести готовое название фильма', callback_data='name')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def categories(message):
    
    if message.data == 'categories':
    
        text = 'Выбрать по:'
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("настроению", callback_data='mood')
        item2 = types.InlineKeyboardButton("жанру", callback_data='genre')
        item3 = types.InlineKeyboardButton("популярности", callback_data='popular')
        item4 = types.InlineKeyboardButton("случайному порядку", callback_data='random')
        markup.add(item1, item2, item3,item4)
        bot.send_message(message.message.chat.id, text, reply_markup = markup)
    elif message.data == 'mood':
        text = 'Какое у вас настроение?'
        markup = types.InlineKeyboardMarkup(row_width=3)
        mood1 = types.InlineKeyboardButton("веселое", callback_data='fun')
        mood2 = types.InlineKeyboardButton("романтичное", callback_data='romantic')
        mood3 = types.InlineKeyboardButton("грустное", callback_data='sad')
        mood4 = types.InlineKeyboardButton("подавленное", callback_data='tired')
        mood5 = types.InlineKeyboardButton("праздичное", callback_data='festive')
        markup.add(mood1, mood2, mood3, mood4, mood5)
        bot.send_message(message.message.chat.id, text, reply_markup = markup)
    elif message.data == 'genre':
        text =  'Выберите жанр, пожалуйста'
        markup = types.InlineKeyboardMarkup(row_width=2)
        genre1 = types.InlineKeyboardButton("фантастика/ фэнтези", callback_data='fantastic')
        genre2 = types.InlineKeyboardButton("комедия", callback_data='comedy')
        genre3 = types.InlineKeyboardButton("боевик", callback_data='action')
        genre4 = types.InlineKeyboardButton("драма/мелодрама", callback_data='drama')
        genre5 = types.InlineKeyboardButton("детектив/триллер", callback_data='thriller')
        genre6 = types.InlineKeyboardButton("ужасы", callback_data='horror')
        genre7 = types.InlineKeyboardButton("мультфильмы", callback_data='cartoons')
        markup.add(genre1,genre2,genre3,genre4,genre5,genre6,genre7)
        bot.send_message(message.message.chat.id, text, reply_markup = markup)
    
    elif message.data == 'festive':
        text = 'Выберите тематику праздника, пожалуйста'
        markup = types.InlineKeyboardMarkup(row_width=2)
        festive1 = types.InlineKeyboardButton("Рождество", callback_data='сhristmas')
        festive2 = types.InlineKeyboardButton("Хэллоуин", callback_data='halloween')
        festive3 = types.InlineKeyboardButton("День влюбленных", callback_data='valentines_day')
        festive4 = types.InlineKeyboardButton("9 мая", callback_data='9th_may')
        markup.add(festive1,festive2,festive3,festive4)
        bot.send_message(message.message.chat.id, text, reply_markup = markup)
    elif message.data == 'name':
        text = 'Введите назввние фильма:'
        bot.send_message(message.message.chat.id, text)








# @bot.message_handler()
# def search_name(message):
#     movies_name = message.text
#     result = sql.get_user_info('action', f'{movies_name}')
#     print(result)
    # text = f'Название - {result[1]}, год - {result[2]}, страна - {result[3]}'
    # bot.send_message(message.message.chat.id, text)
# @bot.callback_query_handler(func=lambda call: True)
# def search_name(message):
#     if message.data == 'comedy':
#         for id in range(0,135):
#             text = sql.get_user_info('table',{id})
#             bot.send_message(message.message.chat.id, text)



bot.polling(none_stop=True)