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
    """
    def __init__(self, _id:int , login:str, password:str):
        self.id = _id
        self.login = login
        self.password = password
    
    def __str__(self):
        return f"User<id:{self.id}, login:{self.login}"

    def __repr__(self):
        return f"User Repr<{self.id}, login:{self.login}>"