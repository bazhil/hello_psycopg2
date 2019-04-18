import psycopg2

# Подключаемся к БД
conn = psycopg2.connect(host="localhost", database="employees", user="postgres", password='postgres')

# Return mistake, don't know what's going on. Everything similar to tutorials, and dont'work.
# Traceback (most recent call last):
#   File "C:/Users/home/PycharmProjects/hello_psycopg2/hello_psycopg2.py", line 4, in <module>
#     conn = psycopg2.connect(host="localhost", database="employees", user="postgres", password='postgres')
#   File "C:\Users\home\PycharmProjects\hello_psycopg2\venv\lib\site-packages\psycopg2\__init__.py", line 126, in connect
#     conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
# psycopg2.OperationalError

# Создаем курсор
cur = conn.cursor()

# Создаем таблицу
cur.execute("""CREATE TABLE employees(
                ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Firstname varchar,
                Lastname varchar,
                Salary int,                                        
                )""")

# Наполняем таблицу
cur.execute("INSERT INTO emloyees values(Null, 'Ivan', 'Ivanov', 1000)")
conn.commit()

# Выводим содержимое таблицы
cur.execute("SELECT * FROM employees")
results = cur.fetchall()
print(results)

# Закрываем соединение с БД
conn.close()

