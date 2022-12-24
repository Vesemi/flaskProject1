import logging
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
        if len(str(name)) < 1:
            return f'failed user {name} {surname} name too short'
        if len(str(surname)) < 1:
            return f'failed user {name} {surname} surname too short'

        self.connection = sqlite3.connect(f'{self.name}.db')
        with self.connection:
            self.connection.execute(users.INSERT_USER, (name, surname))
            self.connection.commit()
            return f'Added user {name} {surname}'

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
            self.connection.execute(tasks.DROP_TABLE)
            self.create_tables()

    ##Database tasks functions
    def get_all_tasks(self):
        self.connection = sqlite3.connect(f'{self.name}.db')
        return self.connection.execute(tasks.GET_ALL_TASKS).fetchall()

    def get_task_by_contractor(self, contractor):
        self.connection = sqlite3.connect(f'{self.name}.db')
        with self.connection:
            return self.connection.execute(tasks.GET_ALL_USER_TASKS, (contractor,)).fetchall()

    def add_task(self, name, description, created_by, contractor):
        self.connection = sqlite3.connect(f'{self.name}.db')
        with self.connection:
            self.connection.execute(tasks.INSERT_TASK, (name, description, created_by, contractor))
            self.connection.commit()
