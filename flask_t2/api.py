"""
Api interface 
with Flask and Flask_restful.
"""

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

    def post():
        pass
    def put():
        pass
    def delete():
        pass

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
# Продолжить лекция №5.
if __name__ == '__main__':
    app.run(port=8080, debug=True)
