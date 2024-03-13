# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import psycopg2
# import psycopg2.extras
#
# app = FastAPI()
#
# # Параметры подключения к базе данных PostgreSQL
#
# # DATABASE_URL = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='name')
# # Модель данных для пользователя
# class User(BaseModel):
#     login: str
#     password: str
#     email: str
#
# # Функция для создания подключения к базе данных
# def get_db_connection():
#     conn = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='name')
#     return conn
#
# # @app.on_event("startup")
# def startup():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id SERIAL PRIMARY KEY,
#             login VARCHAR(255) NOT NULL UNIQUE,
#             password VARCHAR(255) NOT NULL,
#             email VARCHAR(255) NOT NULL UNIQUE
#         );
#     """)
#     conn.commit()
#     cursor.close()
#     conn.close()
#
#
# # Метод для регистрации пользователя
# @app.post("auth/registration", status_code=200)
# def register_user(user: User):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("INSERT INTO users (login, password, email) VALUES (%s, %s, %s)", (user.login, user.password, user.email))
#         conn.commit()
#     except psycopg2.IntegrityError:
#         conn.rollback()
#         raise HTTPException(status_code=400, detail="Email already registered")
#     finally:
#         cursor.close()
#         conn.close()
#     return {"message": "User registered successfully"}
#
# # Метод для получения списка пользователей
# # @app.get("/auth/authentication", status_code=200)
# # def get_users():
# #     conn = get_db_connection()
# #     cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# #     try:
# #         cursor.execute("SELECT * FROM users")
# #         users = cursor.fetchall()
# #     except Exception as e:
# #         raise HTTPException(status_code=500, detail=str(e))
# #     finally:
# #         cursor.close()
# #         conn.close()
# #     return {"users": [dict(user) for user in users]}
