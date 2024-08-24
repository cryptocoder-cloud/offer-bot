# -*- coding: utf8 -*-
"""
Автор: crypto_coding
Дата создания: 24.08.2024
"""
from loguru import logger
from aiogram.utils import executor

from back import dp
from handlers import register, client, inline


register.register_handler(dp)
client.client_handler(dp)
inline.inline_handler(dp)


async def on_startup(_):
    logger.success('Bot Online')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
