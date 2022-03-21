"""
Написать описание модуля.
"""
from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, "Alex", "abcdefg"),
    User(2, "Bob", "qwerty123")
]

# Продолжить с лек 6