import sqlite3

import database_tasks as tasks
import database_users as users


class Database:
    def __init__(self, database_name):
        self.name = database_name
        self.connection = sqlite3.connect(f'{database_name}.db')

    def create_tables(self):
        with self.connection:
            self.connection.execute(users.CREATE_TABLE)
            self.connection.execute(tasks.CREATE_TABLE)

    def add_user(self, name, surname):
        self.connection = sqlite3.connect(f'{self.name}.db')
        with self.connection:
            self.connection.execute(users.INSERT_USER, (name, surname))
            self.connection.commit()

    def get_all_users(self):
        self.connection = sqlite3.connect(f'{self.name}.db')
        return self.connection.execute(users.GET_ALL_USERS).fetchall()

    def get_user_by_name(self, name):
        with(self.connection):
            return self.connection.execute(users.GET_USER_BY_NAME, (name,)).fetchall()

    def get_user_by_surname(self, surname):
        with(self.connection):
            return self.connection.execute(users.GET_USER_BY_SURNAME, (surname,))

    def get_user_by(self, column_name, value):
        with(self.connection):
            return self.connection.execute(users.GET_USER_BY, (column_name, value))

    def drop(self):
        with(self.connection):
            self.connection.execute(users.DROP_TABLE)
            self.create_tables()
