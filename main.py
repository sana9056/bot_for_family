import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6213857128:AAENvQ87pNatvEW2ZU-VWFk7F51ufdHNm9Q')
chat_id = -1001922515746


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, как дела?')


@bot.message_handler(content_types=['text'])
def reply_to_message(message):
    if message.text == "Привет":
        bot.send_message(chat_id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(chat_id, "Задай свой вопрос прямо здесь и я попробую на него ответить.")
    elif message.text == "/button@Lukianenko_bot":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кнопка")
        markup.add(item1)
        bot.send_message(chat_id, 'Выберите кнопку', reply_markup=markup)
    elif message.text == "Кнопка":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Go to Habr", url="https://habr.com/"))
        bot.send_message(chat_id, 'Выберите что вам надо', reply_markup=markup)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("Кнопка 2")
        markup.add(item2)
        bot.send_message(chat_id, 'Выберите кнопку', reply_markup=markup)
    elif message.text == "Кнопка 2":
        bot.send_message(chat_id, 'Спасибо за прочтение статьи!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Кнопка")
        markup.add(item1)
        bot.send_message(chat_id, 'Выберите кнопку', reply_markup=markup)
    elif message.text.lower().startswith('бот'):
        bot.reply_to(message, 'Вы обратились ко мне, нужна помощь?')
    #else:
    #    bot.send_message(chat_id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
