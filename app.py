from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_login import LoginManager
from forms import *
import database
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
database = database.Database('users')
database.create_tables()
database.drop()
app.debug = True


@app.route('/')
def index():
    return render_template("content.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Logowanie', form=form)


@app.route('/users', methods=['GET', 'POST'])
def users():
    form = AddUser()
    if form.validate_on_submit():
        flash(database.add_user(form.name.data, form.surname.data))
    return render_template("users.html", people=database.get_all_users(), form=form)


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    form = AddTask()
    if form.validate_on_submit():
        flash('baanananna')
        database.add_task(form.task_name.data, form.task_description.data,
                          form.task_creator.data, form.task_contractor.data)

    return render_template("tasks.html", tasks=database.get_all_tasks(), form=form)


@app.route('/xd')
def xd():
    return render_template("xd.html")


if __name__ == "__main__":
    app.run(debug=True)
