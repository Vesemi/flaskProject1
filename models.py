from datetime import datetime
from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.body}>'


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(512))
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))
    contractor = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    timestamp_finished = db.Column(db.DateTime, index=True, default=None)
    comment = db.Column(db.String(512))

    def __repr__(self):
        return f'<Task {self.name}>'
