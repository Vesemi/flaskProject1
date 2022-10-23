CREATE_TABLE = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name, surname);"

INSERT_USER = "INSERT INTO users (name, surname) VALUES (?, ?);"

GET_ALL_USERS = "SELECT * FROM users;"



GET_USER_BY_NAME = "SELECT * FROM users WHERE name = ?;"

GET_USER_BY_SURNAME = "SELECT * FROM users WHERE surname = ?;"

GET_USER_BY = "SELECT * FROM users WHERE ? = ?;"


def add_user(connection, name, surname):
    with connection:
        connection.execute(INSERT_USER, (name, surname))
        connection.commit()


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

