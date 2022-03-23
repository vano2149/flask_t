"""
API - crete database and connection.
flask_restful
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
#from auth_conf import authenticate, identity
import os
#from user import UserRegisterResourse

# Сущность приложения
app = Flask(__name__)

# Секретный ключ приложения.
app.secret_key = os.environ.get('SECRET_KEY') or '1234567890'

#Сущность API.

api =Api(app)

#Сущность менеджера токенов.
#jwt =JWT(app, authenticate_handler=authenticate, identity_handler=identity)

# сущьность БД
db =[]

# Ресурс Item /item/<string:name>
class Item(Resource):
    """
    Ресурс, отвечающий за работу с ОДНОЙ товарной единицей
    Реализует CRUD.
    """
    def get(self, name):
        """
        GET /item/<staring:name> - возврашает информацию про товар с именем name.
        """
        item =next(filter(lambda x : x['name'] == name , db), None)
        if item:
            return {"item", item}, 200
        return{"Error" : "Item with that name not found"}, 404
    def post():
        """
        POST /item/<string:name> - создает товар с именем name
        """
        pass
    def put():
        """

        """
        pass
    def delete():
        """

        """
        pass
class ItemCollections(Resource):
    """
    """
    def get(self):
        """
        """
        return {"database" : db}, 200 

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemCollections,'/items')
if __name__ == '__main__':
    app.run(port=8080, debug=True)