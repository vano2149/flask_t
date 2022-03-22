"""
Modul user.py
"""

class User:
    """
    class User:
    atters:
        * id - user ID
        * login - User login
        * password - a clean password user.
    
    Как вы будите делать в жизни:
    attrs:
        * id - user ID
        * login - User login
        * password_hash - это строка, полученная на основе чистого пароля пользователя,
        но дополнительно закодированная при помощи каких-либо алгоритмов.

    Пример:
    login : Vasya2233
    password : 12345qwer
    password_hash : 73u92uhd273gd23iucdh2y3ghf274gf34hfhf34yf2y2f8yh23fh2093f298yhf2p938yf239yhf2937f2
    """
    def __init__(self, _id:int , login:str, password:str):
        self.id = _id
        self.login = login
        self.password = password
    
    def __str__(self):
        return f"User<id:{self.id}, login:{self.login}"

    def __repr__(self):
        return f"User Repr<{self.id}, login:{self.login}>"