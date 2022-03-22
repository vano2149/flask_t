"""
Написать описание модуля.
"""
from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, "Alex", "abcdefg"),
    User(2, "Bob", "qwerty123")
]

# 2-а метода для бд (в виде списков)
# Возвращает все логины
user_logins = {u.login: u for u in users}
# Возвращаем id
user_ids = {u.id : u for u in users}

# По login пытаемя найти пользовалетя в бд.
# Если такой имеется - то сравниваем его пароль и пароль в БД.
# В случае если все ok  - возвращаем данного пользователя.
def authenticate(user_login:str, user_password:str):
    """
    user_login - это данные, с которыми пользователь к нам пришел (его логин).
    user_password - это пароль с которым к нам пришел пользователь.
    """
    # находим пользователя в бд по login.
    user = user_logins.get(user_login, None)
    # Проверяем, что пользователь не None и что его пароль совпадает с паролем в бд.
    if user and safe_str_cmp(user.password, user_password):
        return user


# Функция, которая будет отдавать пользователя по id
def identity(payload:dict):
    _id = payload["identity"]
    return user_ids.get(_id, None)