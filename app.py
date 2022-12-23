from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_login import LoginManager
from forms import LoginForm
import database
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
database = database.Database('users')
database.create_tables()
database.drop()


@app.route('/')
def index():
    return render_template("content.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Logowanie', form=form)


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
                               name=database.add_task(form_data['task_name'],
                                                      form_data['task_description'],
                                                      form_data['task_creator'],
                                                      form_data['task_contractor']),
                               tasks=database.get_all_tasks())

    else:
        return render_template("tasks.html", tasks=database.get_all_tasks())


@app.route('/xd')
def xd():
    return render_template("xd.html")


if __name__ == "__main__":
    app.run(debug=True)
