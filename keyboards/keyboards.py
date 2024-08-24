# -*- coding: utf8 -*-
"""
Автор: crypto_coding
Дата создания: 24.08.2024
"""
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton


async def main():
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    mem = KeyboardButton('🔥 Предложить мем')
    news = KeyboardButton('📣 Предложить новость')
    feedback = KeyboardButton('🤙 Связаться с администратором')
    key.row(mem, news)
    key.row(feedback)
    return key


async def cancel():
    key = InlineKeyboardMarkup()
    key.row(InlineKeyboardButton(text='❌ Отмена', callback_data='cancel'))
    return key


async def mem():
    key = InlineKeyboardMarkup()
    mem = InlineKeyboardButton(text='🔥 Предложить мем', callback_data='add_mem')
    key.row(mem)
    return key


async def news():
    key = InlineKeyboardMarkup()
    news = InlineKeyboardButton(text='📣 Предложить новость', callback_data='add_news')
    key.row(news)
    return key
