from datetime import datetime
from extensions import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='contractor', foreign_keys="[Task.contractor_id]")
    tasks2 = db.relationship('Task', backref='creator', foreign_keys="[Task.creator_id]")
    last_seen = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return f'{self.username}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Integer, db.ForeignKey('task.id'))
    text = db.Column(db.String(512))
    creator = db.Column(db.Integer)
    timestamp_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    description = db.Column(db.String(512))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    contractor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    timestamp_finished = db.Column(db.DateTime, index=True, default=None)
    comment = db.relationship('Comment', backref='comments')

    def __repr__(self):
        return f'{self.title}'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))