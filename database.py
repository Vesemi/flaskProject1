import sqlite3














def connect():
    return sqlite3.connect("users.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_USERS_TABLE)


def add_user(connection, name, surname):
    with connection:
        connection.execute(INSERT_USER, (name, surname))


def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()


def get_user_by_name(connection, name):
    with(connection):
        return connection.execute(GET_USER_BY_NAME, (name,)).fetchall()


def get_user_by_surname(connection, surname):
    with(connection):
        return connection.execute(GET_USER_BY_SURNAME, (surname,))


def get_user_by(connection, column_name, value):
    with(connection):
        return connection.execute(GET_USER_BY, (column_name, value))

