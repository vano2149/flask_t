"""
Подключение к субд.
"""

import sqlite3


#Подключение к субд (реальное)
# conn - это объект подключения к бд. Выполняется проверка предварительных данных,
# создание файла в случае отсутствия, и PING базы данных. 
conn = sqlite3.connect("data.db")

# Интерфейс бд.
# cursor - это объект интерфейса СББД, 
# через него будут проходить все запросы и обращения.
cursor = conn.cursor()

# Первая команда - создать какую-нибуть таблицу.
create_query = 'CREATE TABLE IF NOT EXISTS user (id INTEGER RYMARY KEY, login TEXT, password TEXT)'
# Запрос пишется в виде одной строки, содержащей команды, понятные языку SQL.
# Выполняем Запрос.
cursor.execute(create_query, params)
# query - сам запрос
# params - Это кортеж с параметром (будут подставленны на место "?" в вашем запросе)

# Сохраняем изменения
conn.commit()

# Вторая команда - добавим пользователя
user = ('Alex' , "qwert123")
insert_query = 'INSERT INTO user VALUES(NULL, ?, ?)' # ? - placeholder для 
#дальнейших параметров, передаваемых на этапе выполнения запроса.
# Теперь выполним запрос и передадим параметры.

for i in range(1, 1000):
    cursor.execute(insert_query, user)
    # Сохраним изменения.
conn.commit() # - сохраняем текущего состаяния таблиц.

# Третья команда - проверим, что в бд что-то появилось
select_query = 'SELECT * FROM user'
for row in cursor.execute(select_query):
    print(row)
# Отключаемся от БД.
conn.close() # - "разрыв" соединения с бд (безопасное закрытее соединения)
