from flask_login import LoginManager, UserMixin
from core import db, app
from enum import Enum

class Tags(Enum):
    USER = 1
    TRAINER = 2
    ADMIN = 3

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String(320), unique=True, index=True)
    username = db.Column(db.String(320), unique=True, index=True)
    password = db.Column(db.String(320))
    tags = db.relationship('Tag', backref='user', lazy='dynamic')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Enum(Tags), default=Tags.USER)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# flask_login
login = LoginManager(app)
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))