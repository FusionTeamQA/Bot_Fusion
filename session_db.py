import psycopg2
from config_db import host, user, password, db_name


def connect_db():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
    )
    cursor = connection.cursor()


def connect_close():
    connection.close()
