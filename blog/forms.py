from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[Length(min=3 , max=20, message='Kullanıcı adı 3-20 karakter uzunluğunda olmalıdır.'), DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password' , validators=[Length(min=5, max=30, message='Parola uzunluğu 5-30 karakter arasında olmalıdır.'), DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Submit',validators=[DataRequired()])

class PostCreateForm(FlaskForm):
    title = StringField(label='Title', validators=[Length(max=25), DataRequired()])
    content = TextAreaField(label='Content', validators=[DataRequired()])
    author = StringField(label='Author', validators=[Length(max=25), DataRequired()])
    submit = SubmitField(label='Submit',validators=[DataRequired()])

class SubscribeForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    submit = SubmitField(label='Submit', validators=[DataRequired()])
