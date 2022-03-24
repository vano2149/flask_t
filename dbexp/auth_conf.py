"""
Конфигурация User.
"""
from user import UserModel
from werkzeug.security import safe_str_cmp

def authenticate(username:str, password:str):
    """
    """
    user = UserModel.search_by_name(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload:dict):
    """
    """
    _id = payload["identity"]
    return UserModel.search_by_id(_id)