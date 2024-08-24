# -*- coding: utf8 -*-
"""
Автор: crypto_coding
Дата создания: 24.08.2024
"""
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode

from config import token


db = sqlite3.connect('database/bot.db', check_same_thread=False)
sql = db.cursor()


bot = Bot(token=token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
