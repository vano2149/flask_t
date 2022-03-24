"""
Пакет с моделью поьзователя.
"""
import sqlite3
from flask_restful import Resource, reqparse


# Модель пользователя - класс, отражающий схему хранения объекта в чем-либо (бд, файл)
class UserModel:
    """
    Модель пользователя
    attrs:
        * id
        * username
        * password
    """
    # Внешний классовый атрибут
    __tablename__ = "users"

    def __init__(self, _id:int, username:str, password:str):
        """
        Конструктор.
        """
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def search_by_name(cls, username:str):
        """
        Метод пытается найти в бд кого-то с именем username
        и вернуть UserModel() c этим username.
        """
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        select_query = f"SELECT * FROM {cls.__tablename__} WHERE username=?"
        sql_row = cursor.execute(select_query, (username,)).fetchone()
        if sql_row:
            user = cls(sql_row[0], sql_row[1],sql_row[2])
        else:
            user = None
        
        conn.close()
        return user

    
    @classmethod
    def search_by_id(cls, _id):
        """
        Метод пытается найти в бд кого-то с _id
        и вернуть UserModel() с этим id
        """
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        select_query = f"SELECT * FROM {cls.__tablename__} WHERE id=?"
        sql_row = cursor.execute(select_query,(_id,)).fetchone()
        if sql_row:
            user = cls(sql_row[0], sql_row[1], sql_row[2])
        else:
            user = None

        conn.close()
        return user



