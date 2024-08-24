# -*- coding: utf8 -*-
"""
Автор: crypto_coding
Дата создания: 24.08.2024
"""
from aiogram.types import Message

from back import sql, db


async def check_register(user_id):
    sql.execute(f'SELECT username FROM users WHERE id={user_id}')
    rec = sql.fetchall()

    if rec:
        return True
    return False


async def insert(message: Message):
    sql.execute("INSERT OR IGNORE INTO users VALUES (?, ?)",
                (message.from_user.id, message.from_user.username))
    db.commit()


async def get_all_id():
    sql.execute('SELECT id FROM users')
    rec = sql.fetchall()

    all_id = []
    for i in rec:
        all_id.append(i[0])
    return all_id
