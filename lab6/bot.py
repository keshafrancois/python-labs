import telebot
import requests

bot = telebot.TeleBot('5824153383:AAGhQWOvYcAeuzfmyyhrXdNLP7DzZhcWEZ0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши /help , чтобы узнать что может бот!')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Этот бот присылает тебе абсолютно случайную картинку. Для этого просто напиши /img')

@bot.message_handler(commands=['img'])
def number(message):
    r = requests.get('https://random.imagecdn.app/700/500')
    q = r.url
    bot.send_photo(message.chat.id, q)


bot.polling(none_stop=True)