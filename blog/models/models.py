from blog import db, bcrypt, login_manager, migrate
from flask_login import UserMixin
from time import localtime

@login_manager.user_loader
def load_user(member_id):
    return Member.query.get(int(member_id))


def create_time(day=localtime().tm_mday , month=localtime().tm_mon , year=localtime().tm_year):
    return f'{day}.{month}.{year}'

class Member(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=20), unique=True, nullable=False)
    email = db.Column(db.String(length=120), unique=True, nullable=False)
    password = db.Column(db.String(length=100), nullable=False)

    def __repr__(self):
        return f'<Username: {self.username}, Email: {self.email}.>'

    def get_id(self):
        return self._id

    def hash_password(self, input_password):
        return bcrypt.generate_password_hash(input_password).decode('utf-8')

    def __init__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.password, input_password)


class Post(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=25), nullable=False, unique=True)
    content = db.Column(db.Text() , nullable=False)
    author = db.Column(db.String(length=25), nullable=False)
    created_time = db.Column(db.String(length=10))

    def __repr__(self):
        return f'< Post Title:{self.title}, Post Author:{self.author}. >'

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_time = create_time(localtime().tm_mday , localtime().tm_mon , localtime().tm_year)

    def get_id(self):
        return self._id
