import psycopg2


# Подключение к БД
conn = psycopg2.connect(host='localhost', user='postgres', password='10121991', dbname='kapinuss')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            login VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE )''')

# Вводим значения в БД
login = input("Введите имя: ")
password= input("Введите пароль: ")
email = input("Введите email")
cursor.execute("INSERT INTO users (login, password, email) VALUES (%s, %s, %s)", (login, password, email))
conn.commit()

# Проверка, что запись добавилась
cursor.execute("SELECT * FROM users WHERE login = %s AND password = %s AND email = %s", (login, password, email))
result = cursor.fetchone()
if result:
    print("Запись успешно добавлена")
    status = 201
else:
    print("Ошибка при добавлении записи")
    status = 404

# Закрываем соединение с БД
conn.close()



