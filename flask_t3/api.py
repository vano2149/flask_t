"""
Create an easy API interface with 
flask, flask_restful and to realize 
authrnticate func.
"""

from flask import Flask, request
from flask_restful import Resource, Api , reqparse

#Сущьность приложения.
app = Flask(__name__)

# сущьность API
api = Api(app)

# сущьность БД
db = []

#Ресурсе Item/item/<string:name>
class Item(Resource):
    """
    Ресурс, отвечающий за работу с Одной товарной единицей
    Реализирует CRUD.
    """
    parser = reqparse.RequestParser()
    # Price ОБЯЗАТЕЛЬНО type = float
    parser.add_argument("price", type=float, required=True, help="Field 'price' required float value!")
    # Нам ОБЯЗАТЕЛЬНО НУЖЕН amount типа int
    parser.add_argument("amount", type = int, required=True, help="This field required int value!")

    def get(self, name):
        """
        GET /item/<string:name> - Возвращаем информацию 
        про товар с именем name
        """
        item = next(filter(lambda x : x["name"] == name, db), None)
        if item:
            return {"item":item}, 200
        return {'Error' : "Item with that name not Found!"}, 404

    def post(self, name):
        """
        POST /item/<string:name> - создает товар с именем name
        """
        # Проверим, проверим что в бд ЕЩЕ НЕТ товара с таким name
        if next(filter(lambda x : x["name"] == name, db), None):
            return {"Error": f"Item with name {name} already exists!"}, 400
        
        # Теперь парсим тело запроса.
        request_body = Item.parser.parse_args()
        new_item = {"name" : name, "price" : request_body["price"], "amount" : request_body["amount"]}
        db.append(new_item)
        return new_item, 201


    def put(self, name):
        item = next(filter(lambda x : x["name"] == name, db), None)
        if item:
            request_body = Item.parser.parse_args()
            item.update(request_body)
            return item, 202
        return {'Error' : f'Item with name {name} not found'}, 404
    
    def delete(self, name):
        global db
        start_len = len(db)
        db = list(filter(lambda x : x['name'] != name, db))
        if abs(start_len - len(db)) > 0:
            return {'Message' : "Item successfully deleted!"}, 202
        return {'Error' : "Item with that name not found"}, 404

# Ресурс Items/items
class ItemCollection(Resource):
    """
    Ресурсб отвечающий за работу с МНОЖЕСТВОМ товаров
    """