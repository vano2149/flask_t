"""
Модуль для проверки базы данных к работе.
"""
"""
Модуть для подготовки базы данных к работе.
"""
import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()


#Cоздадим таблицу для хранения пользователей.
create_users = 'CREATE TABLE IF EXISTS user (id INTEGER PRYMARY KEY, username TEXT, password TEXT)'
cur.execute(create_users)

conn.commit()
conn.close()