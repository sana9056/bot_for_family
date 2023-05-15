from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from info import bot, chat_id, button, url
import cal

# Получение др в этом месяце
date = cal.get_date_birth()
my_text = ', '.join(date)

# Обьявляю кнопки
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Наше Древо")
item2 = types.KeyboardButton("Дни рождения в этом месяце")
markup.add(item1, item2)



# Стартовая кнопка
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, как дела?', reply_markup=markup)

# Реакции на сообщения и доп.кнопки
@bot.message_handler(content_types=['text'])
def reply_to_message(message):
    if message.text == "Привет":
        bot.send_message(chat_id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(chat_id, "Задай свой вопрос прямо здесь и я попробую на него ответить.")
    elif message.text == "Наше Древо":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("На дерево!", url))
        bot.send_message(chat_id, 'Ниже найдешь ссылку на наше древо семьи', reply_markup=markup)
    elif message.text == "Дни рождения в этом месяце":
        bot.send_message(chat_id, my_text)
    elif message.text.lower().startswith('бот'):
        bot.reply_to(message, 'Вы обратились ко мне, нужна помощь?')
    #else:
    #    bot.send_message(chat_id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
