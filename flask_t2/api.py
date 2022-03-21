"""
Easy Api interface,
with Flask and Flask_restful.
"""

from os import name
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

# сущность приложения
app = Flask(__name__)

# сущность API
api = Api(app)

#сущьность БД
db = []

#Ресурс Item /item/<string:name>
class Item(Resource):
    """
    Ресурс, отвечающий за работу с ОДНОЙ товарной еденицей
    Реализует CRUD.
    """

    # Получаем тело запроса
    # Инициализируется валидатор.
    parser = reqparse.RequestParser()
    # НАМ ОБЯЗАТЕЛЬНО НУЖЕН price типа float
    parser.add_argument("price", type = float, required=True, help="Field 'price' required float value!")
    # НАМ ОБЯЗАТЕЛЬНО НУЖЕН amount типа int
    parser.add_argument("amount", type=int, required=True, help="This field required int value!")

    def get(self, name):
        """
        GET /item/<string:name> - возвращает информацию про товары с именем name
        """
        item = next(filter(lambda x : x["name"] == name, db), None)
        if item:
            return {"item": item}, 200
        return {"Error" : "Item with that name not fount"}, 404

    def post(self, name):
        """
        POST /item/<string:name> - создает товар с менем name
        """
        # Проверим б что в бд ЕЩЕ НЕТ товара с таким именем.
        if next(filter(lambda x : x["name"] == name, db), None):
            return {'Error' : f'Item with name {name} alredy exists!'}, 400
        #Теперь парсим тело запроса
        request_body = Item.parser.parse_args()
        new_item = {"name" : name, "price" : request_body["price"], "amount" : request_body["amount"]}
        db.append(new_item)
        return new_item, 201
    def put(self, name):
        """
        PUT /item/<staring:name> - Изменение СУЩЕСТВУЮЩЕГО товара.
        """
        item = next(filter(lambda x : x["name"] == name, db), None)
        if item:
            request_body = Item.parser.parse_args()
            item.update(request_body)
            return item, 202
        return {'Error' : f"Item wthi name {name} not found"}, 404
    def delete(self, name):
        """
        DELETE /item/<staring:name> - Удаление элемента списка магазина.
        """
        global db
        start_len = len(db)
        db = list(filter(lambda x : x["name"] != name, db))
        if abs(start_len - len(db)) > 0 :
            return {"Message" : "Item successfully deleted"}, 202
        return {"Error" : "Item with that name not found"}, 404
        
# Ресурс Items /items
class ItemCollection(Resource):
    def get(self):
        """
        Ресурс, отвечающий за работу с МНОЖЕСТВОМ товаров. 
        """
        return {"database": db}, 200


#Добавим ресурс к API
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemCollection, '/items')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
