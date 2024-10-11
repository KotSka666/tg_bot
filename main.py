from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
# from db11 import * as gb
import db11 as gb
import requests
import sqlite3

TOKEN = "7702169434:AAGuLqX-SePEwuRixwhg4cc6WQ0-WEp4YDY"

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def button_magazin(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('За день', callback_data="day")
    item2 = types.InlineKeyboardButton('За последние 7 дней', callback_data="week")
    item3 = types.InlineKeyboardButton('За месяц', callback_data="month")
    item4 = types.InlineKeyboardButton('За пред месяц', callback_data="months")
    item5 = types.InlineKeyboardButton('За год', callback_data="year")
    item6 = types.InlineKeyboardButton('За все время', callback_data="all")
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(5205925660, "Выбирай", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'day':
        summ1 = gb.get_recorts_day()[0]
        summ2 = gb.get_recorts_day()[1]
        summ3 = gb.get_recorts_day()[2]
        bot.send_message(5205925660, f"За День\nЧепух: {summ1}\nПух: {summ2}\nОбщее: {summ3}")
    elif call.data == 'week':
        summ1 = gb.get_recorts_week()[0]
        summ2 = gb.get_recorts_week()[1]
        summ3 = gb.get_recorts_week()[2]
        bot.send_message(5205925660, f"За Неделю\nЧепух: {summ1}\nПух: {summ2}\nОбщее: {summ3}")
    elif call.data == 'month':
        summ1 = gb.get_recorts_monch()[0]
        summ2 = gb.get_recorts_monch()[1]
        summ3 = gb.get_recorts_monch()[2]
        bot.send_message(5205925660, f"За Месяц\nЧепух: {summ1}\nПух: {summ2}\nОбщее: {summ3}")
    elif call.data == 'months':
        summ1 = gb.get_recorts_monchs()[0]
        summ2 = gb.get_recorts_monchs()[1]
        summ3 = gb.get_recorts_monchs()[2]
        bot.send_message(5205925660, f"За пред Месяц\nЧепух: {summ1}\nПух: {summ2}\nОбщее: {summ3}")
    elif call.data == 'year':
        summ1 = gb.get_recorts_year()[0]
        summ2 = gb.get_recorts_year()[1]
        summ3 = gb.get_recorts_year()[2]
        bot.send_message(5205925660, f"За Год\nЧепух: {summ1}\nПух: {summ2}\nОбщее: {summ3}")
    elif call.data == 'all':
        summ1 = gb.get_recorts_all()[0]
        summ2 = gb.get_recorts_all()[1]
        summ3 = gb.get_recorts_all()[2]
        bot.send_message(5205925660, f"За Все время\nЧепух: {summ1}\nПух: {summ2}\nОбщее: {summ3}")





bot.polling(non_stop=True)


