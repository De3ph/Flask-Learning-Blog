from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databases/blog.db'
app.config['SECRET_KEY'] = 'bed6e0c2b4b5c3fd9007539d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'selfudemycourse@gmail.com'
app.config['MAIL_PASSWORD'] = 'Roadtosucces100'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'selfudemycourse@gmail.com'



db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

migrate = Migrate(app, db , render_as_batch=True)

mail = Mail(app)

from blog.routes import route
