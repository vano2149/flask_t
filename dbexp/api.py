"""
API - crete database and connection.
flask_restful
"""

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from auth_conf import authenticate, identity
import os
from user import UserRegisterResourse

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
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Field 'price' required float value!")
    parser.add_argument('amount', type=int, required=True, help="This field required int value")

    def get(self, name):
        """
        GET /item/<staring:name> - возврашает информацию про товар с именем name.
        """
        item =next(filter(lambda x : x['name'] == name , db), None)
        if item:
            return {"item", item}, 200
        return{"Error" : "Item with that name not found"}, 404

    def post(self, name):
        """
        POST /item/<string:name> - создает товар с именем name
        """
        if next(filter(lambda x : x['name'] == name, db),None):
            return {'Error': f'Item with name {name} already exists!'}, 400

        request_body = Item.parser.parse_args()
        new_item = {"name" : name, "price": request_body["price"], "amount": request_body["amount"]}
        db.append(new_item)
        return new_item, 201

    def put(self, name):
        """
        PUT /item/<string:name>
        """
        item = next(filter(lambda x : x['name'] == name, db),None)
        if item:
            request_body=Item.parser.parse_args()
            item.update(request_body)
            return item, 202
        return {'Error' : f"Item with name {name} not found"}, 404

    def delete(self, name):
        """
        DELETE /item/<string:name>
        """
        global db
        start_len = len(db)
        db = list(filter(lambda x : x["name"] != name, db))
        if abs(start_len - len(db)) > 0:
            return {"Message" : "Item successfule deleted!"}, 202
        return {"Error" : f"Item with that name {name} not found!"}, 404

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
    import table
    app.run(port=8080, debug=True)