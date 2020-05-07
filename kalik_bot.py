import telebot
from telebot import apihelper, TeleBot
import parser_data

apihelper.proxy = {'proxy set'}

bot: TeleBot = telebot.TeleBot('botTOKEN')


@bot.message_handler(commands=['start'])
def send_start_message(message):
    bot.send_message(message.chat.id, 'Чтобы узнать, что я могу, введи /help')


@bot.message_handler(commands=['help'])
def send_start_message(message):
    bot.send_message(message.chat.id, 'Пока я умею парсить только статистику по запросу.\n'
                                      'Для того, чтобы её вывести, введите:\n'
                                      '/covidvl - статистика по Приморскому краю от vl.ru\n'
                                      '/stopcovid - статистика по России от стопкоронавирус.рф')


@bot.message_handler(commands=['covidvl'])
def send_statistics_vlru(message):
    bot.send_message(message.chat.id, parser_data.get_data_from_vlru())


@bot.message_handler(commands=['stopcovid'])
def send_statistics_vlru(message):
    bot.send_message(message.chat.id, parser_data.get_data_from_stopcovid())


if __name__ == '__main__':
    bot.infinity_polling()
