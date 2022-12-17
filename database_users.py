CREATE_TABLE = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name, surname);"

INSERT_USER = "INSERT INTO users (name, surname) VALUES (?, ?);"

GET_ALL_USERS = "SELECT * FROM users;"

GET_USER_BY_NAME = "SELECT * FROM users WHERE name = ?;"

GET_USER_BY_SURNAME = "SELECT * FROM users WHERE surname = ?;"

GET_USER_BY = "SELECT * FROM users WHERE ? = ?;"

DROP_TABLE = "DROP TABLE IF EXISTS users;"


