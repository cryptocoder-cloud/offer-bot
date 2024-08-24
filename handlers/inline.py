# -*- coding: utf8 -*-
"""
Автор: crypto_coding
Дата создания: 24.08.2024
"""
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import TelegramAPIError
from loguru import logger

from handlers.client import Upload
from keyboards import keyboards as key
from text import dialogues


async def cancel(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer('❌ Отмена')
    await call.message.delete()


async def add_mem(call: CallbackQuery):
    await call.message.edit_text(text=dialogues.state_text, reply_markup=await key.cancel())
    await Upload.mem.set()


async def add_news(call: CallbackQuery):
    await call.message.edit_text(text=dialogues.state_text, reply_markup=await key.cancel())
    await Upload.news.set()


async def main_inline_handler(call: CallbackQuery, state: FSMContext):
    logger.debug(f"Received callback: {call.data}")

    callback = call.data.split('|')[0] if '|' in call.data else call.data

    call_dict = {
        'cancel': cancel,
        'add_mem': add_mem,
        'add_news': add_news,
    }

    call_function = call_dict.get(callback)

    if call_function is None:
        logger.error(f"Ошибка в inline handlers: не смог определить функцию для callback '{callback}'")
        await call.answer("Произошла ошибка. Пожалуйста, попробуйте еще раз.")
        return

    # Функции состояния
    state_functions = ['cancel',]

    try:
        if callback in state_functions:
            await call_function(call, state)
        else:
            await call_function(call)
    except TelegramAPIError as e:
        logger.error(f"Ошибка при выполнении функции '{callback}': {e}")
        await call.answer("Произошла ошибка при выполнении вашего запроса.")


def inline_handler(dp: Dispatcher):
    dp.register_callback_query_handler(main_inline_handler, state='*')
