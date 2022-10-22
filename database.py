import sqlite3
import database_tasks as tasks, database_users as users


def connect():
    return sqlite3.connect("users.db")


def create_tables(connection):
    with connection:
        connection.execute(users.CREATE_TABLE)
        connection.execute(tasks.CREATE_TABLE)



