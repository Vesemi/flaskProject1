from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from forms import *
from models import *
from config import Config
from flask_migrate import Migrate
from extensions import db, login
from werkzeug.urls import url_parse

app = Flask(__name__)
app.config.from_object(Config)
login.init_app(app)
login.login_view = 'login'


@app.route('/')
@app.route('/index')
def index():
    return render_template("content.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    return render_template("users.html", people=User.query.all())


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = AddTask()
    if form.validate_on_submit():
        task = Task(title=form.title.data, description=form.description.data,
                    creator=form.creator.data, contractor=form.contractor.data)
        db.session.rollback()
        db.session.add(task)
        db.session.commit()
    return render_template("tasks.html", tasks=Task.query.all(), form=form)


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


register_extensions(app)

if __name__ == "__main__":
    app.run(debug=True)
