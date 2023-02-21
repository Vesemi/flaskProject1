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
            flash('Nieprawidłowe hasło bądź login!')
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
        flash('Rejestracja poprawna')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    return render_template("users.html", users=User.query.all())


@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    print([r.username for r in User.query.all()])
    form2 = TaskButtons()
    comment_form = AddComment()
    return render_template("tasks.html", tasks=Task.query.all(), form2=form2, comment_form=comment_form)


@app.route('/addtask', methods=['GET', 'POST'])
@login_required
def addtask():
    form = AddTask()
    form.contractor.choices = [r.username for r in User.query.all()]
    form.creator.data = current_user
    if form.validate_on_submit():
        contractor = User.query.filter_by(username=form.contractor.data).first_or_404()
        creator = User.query.filter_by(username=str(current_user)).first_or_404()
        task = Task(title=form.title.data, description=form.description.data,
                    creator_id=creator.id, contractor_id=contractor.id,
                    timestamp_deadline=form.timestamp_deadline.data)
        db.session.rollback()
        db.session.add(task)
        db.session.commit()
        flash(f'Zadanie {task.title} zostało pomyślnie dodane!')
    return render_template("addtask.html", form=form)


@app.route('/edittask/<int:id>', methods=['GET', 'POST'])
@login_required
def edittask(id):
    form = EditTask()
    form.contractor.choices = [r.username for r in User.query.all()]
    if form.submit.data:
        if form.validate_on_submit():
            task = Task.query.filter_by(id=id).first()
            contractor = User.query.filter_by(username=form.contractor.data).first_or_404()
            task.contractor_id = contractor.id
            task.description = form.description.data
            task.title = form.title.data
            db.session.commit()
            return redirect(url_for('tasks'))

    else:
        task = Task.query.filter_by(id=id).first()
        contractor = User.query.filter_by(id=task.contractor_id).first_or_404()
        creator = User.query.filter_by(id=task.creator_id).first_or_404()
        form.creator.data = creator.username
        form.contractor.data = contractor.username
        form.description.data = task.description
        form.title.data = task.title
        form.timestamp_created.data = task.timestamp_created
        form.timestamp_deadline.data = task.timestamp_deadline

        return render_template("edittask.html", form=form, id=id)


@app.route('/deletetask/<int:id>', methods=['GET', 'POST'])
@login_required
def deletetask(id):
    Task.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('tasks'))


@app.route('/finishtask/<int:id>', methods=['GET', 'POST'])
@login_required
def finishtask(id):
    task = Task.query.filter_by(id=id).first()
    task.timestamp_finished = datetime.utcnow()
    db.session.commit()
    return redirect(url_for('tasks'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    tasks = user.tasks
    return render_template('user.html', user=user, tasks=tasks)


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)


register_extensions(app)

if __name__ == "__main__":
    app.run(debug=True)
