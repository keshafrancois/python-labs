import telebot
import requests

bot = telebot.TeleBot('5824153383:AAGhQWOvYcAeuzfmyyhrXdNLP7DzZhcWEZ0')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, напиши /help , чтобы узнать что может бот!')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Этот бот присылает тебе случайное число и так же небольшой факт о нем. Для этого просто напиши /number')

@bot.message_handler(commands=['number'])
def number(message):
    r = requests.get('http://numbersapi.com/random/math')
    url = r.url
    bot.send_message(message.chat.id, url)


bot.polling(none_stop=True)