# -*- coding: utf8 -*-
"""
Автор: crypto_coding
Дата создания: 24.08.2024
"""
import config

from aiogram import Dispatcher
from aiogram.types import Message

from back import bot
from database import database as base
from keyboards import keyboards as key
from text import dialogues
from handlers.client import Upload


async def check_group(message: Message):
    try:
        if message.chat.type == 'group' or message.chat.type == 'supergroup':
            await message.reply('Перейдите в личку с ботом.')
            return True
        return False
    except AttributeError:
        return False


async def get_started(message: Message):
    if await check_group(message):
        return

    if not await base.check_register(message.from_user.id):
        await base.insert(message)
        for i in config.admin_id:
            await bot.send_message(i, f'Зарегистрирован новый пользователь: @{message.from_user.username} | {message.from_user.id}')

    await bot.send_message(message.from_user.id, text=dialogues.welcome_message.format(username=message.from_user.username), reply_markup=await key.main())


async def spam_all(message: Message):
    if message.from_user.id in config.admin_id:
        await message.answer('Следущим сообщением пришлите рассылку, для отмены нажмите соответствующую кнопку.', reply_markup=await key.cancel())
        await Upload.spam.set()
    else:
        return message.answer('Доступа нет')


def register_handler(dp: Dispatcher):
    dp.register_message_handler(get_started, commands="start")
    dp.register_message_handler(spam_all, commands="spam")
