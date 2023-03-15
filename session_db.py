import telebot
from telebot import types
import setting
import psycopg2
import os, sys
from config_db import host, user, password, db_name
from requests.exceptions import ConnectionError, ReadTimeout


def connect_db():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(f"Server version: + {cursor.fetchone()}")
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                        id INTEGER,
                        user_first_name varchar(50),
                        user_last_name varchar(50),
                        username varchar(50),
                        data_time varchar(50)
                        )''')
    connection.commit()
    people_id = message.from_user.id
    cursor.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        USER_ID = [message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                   message.from_user.username, dt_string]
        cursor.execute("INSERT INTO users VALUES(%s,%s,%s,%s,%s);", USER_ID)
        connection.commit()
    else:
        print(message.from_user.username)
