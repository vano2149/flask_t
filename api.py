"""
Первая простая API.
С одним запросом GET.
"""

from flask import Flask, jsonify

#сущьность приложения (сервер)
app = Flask(__name__)

# Сущьность бд

db = [
    {
        'name' : 'First_Store',
        'item': [
            {
                'name' : 'First Item',
                'price' : 22.22,
            },
        ]
    },
]

@app.route('/store', methods=['GET'])
def get_stores():
    """
    GET / stores - отдает информацию 
    про все магазины, какие у нас есть.
    """
    return jsonify({"stores" : db}), 200

@app.route('/store/<string:name>', methods=['GET'])
def get_store(name:str):
    """
    GET /store/<string:name> - отдадин информацию 
    про магазин с именем name.
    """
    # Пробегаем циклом по всем магазинам.
    for store in db:
        # Если имя магазина совподает с искомым
        if store["name"] == name:
            #Возвращаем найденный магазин
            return jsonify(store), 200
    # А если не нашли "Вбрасываем исключение"
    return jsonify({"Error" : "Store with that Name not Found"}), 404
if __name__ == "__main__":
    app.run(port=8080, debug=True)