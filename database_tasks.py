CREATE_TABLE = "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, name, description," \
               " task_creator, task_contractor, date_created, date_finished);"

INSERT_TASK = "INSERT INTO tasks (name, description, task_creator, task_contractor, date_created, date_finished)" \
              "VALUES (?, ?, ?, ?, TIME('now'), NULL);"

GET_ALL_TASKS = "SELECT * FROM tasks;"

GET_ALL_USER_TASKS = "SELECT * FROM tasks WHERE task_contractor = ?;"
