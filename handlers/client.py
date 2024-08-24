# -*- coding: utf8 -*-
"""
Автор: crypto_coding
Дата создания: 24.08.2024
"""

import config

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message

from database import database as base
from back import bot, dp
from keyboards import keyboards as key
from text import dialogues


class Upload(StatesGroup):
    mem = State()
    news = State()
    spam = State()


async def check_group(message: Message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        await message.reply('Перейдите в личку с ботом.')
        return True
    return False


async def offer_mem(message: Message):
    await check_group(message)

    await bot.send_message(message.from_user.id, dialogues.mem_text, reply_markup=await key.mem())


async def offer_news(message: Message):
    await check_group(message)

    await bot.send_message(message.from_user.id, dialogues.mem_text, reply_markup=await key.news())


async def feedback(message: Message):
    await check_group(message)

    await bot.send_message(message.from_user.id, dialogues.info)


@dp.message_handler(state=Upload.mem)
async def upload_mem(message: Message, state: FSMContext):
    await state.finish()

    await bot.send_message(config.offer_channel_id, f'<b>🔥Новая предложка мема\nОтправил: @{message.chat.username}</b>')

    await message.forward(config.offer_channel_id)

    await message.answer('✅ Вы успешно отправили мем.')
    return


@dp.message_handler(state=Upload.news)
async def upload_news(message: Message, state: FSMContext):
    await state.finish()

    await bot.send_message(config.offer_channel_id, f'<b>📣Новая предложка новости\nОтправил: @{message.chat.username}</b>')

    await message.forward(config.offer_channel_id)

    await message.answer('✅ Вы успешно отправили новость.')
    return


@dp.message_handler(state=Upload.spam)
async def spam(message: Message, state: FSMContext):
    await state.finish()

    all_id = await base.get_all_id()

    good = []

    for i in all_id:
        try:
            await message.copy_to(i)
            good.append(i)
        except:
            continue

    return await message.answer(f'✅ Рассылка окончена, всего отправлено: {len(good)}')


def client_handler(dp: Dispatcher):
    dp.register_message_handler(offer_mem, Text(equals="🔥 Предложить мем"))
    dp.register_message_handler(offer_news, Text(equals="📣 Предложить новость"))
    dp.register_message_handler(feedback, Text(equals="🤙 Связаться с администратором"))
