from flask import Flask, render_template, request
import database

app = Flask(__name__)
database = database.Database('users')
database.create_tables()
database.drop()


@app.route('/')
def index():
    return render_template("content.html")


@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == "POST":
        form_data = request.form
        return render_template("users.html",
                               name=database.add_user(form_data['name'], form_data['surname']),
                               people=database.get_all_users())

    else:
        return render_template("users.html", people=database.get_all_users())


@app.route('/tasks', methods=['POST', 'GET'])
def tasks():
    if request.method == "POST":
        form_data = request.form
        return render_template("tasks.html",
                               name=database.add_task(form_data['name'],
                                                      form_data['description'],
                                                      form_data['task_creator'],
                                                      form_data['task_contractor']),
                               tasks=database.get_all_tasks())

    else:
        return render_template("tasks.html", people=database.get_all_tasks())


@app.route('/xd')
def xd():
    return render_template("xd.html")


if __name__ == "__main__":
    app.run(debug=True)
