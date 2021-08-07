from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField(label='Kullanıcı Adı', validators=[Length(min=3 , max=20, message='Kullanıcı adı 3-20 karakter uzunluğunda olmalıdır.'), DataRequired()])
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Parola' , validators=[Length(min=5, max=30, message='Parola uzunluğu 5-30 karakter arasında olmalıdır.'), DataRequired()])
    submit = SubmitField(label='Gönder')

class LoginForm(FlaskForm):
    username = StringField(label='Kullanıcı Adı', validators=[DataRequired()])
    password = PasswordField(label='Parola', validators=[DataRequired()])
    submit = SubmitField(label='Submit',validators=[DataRequired()])

class PostCreateForm(FlaskForm):
    title = StringField(label='Başlık', validators=[Length(max=25), DataRequired()])
    content = TextAreaField(label='Yazı', validators=[DataRequired()])
    author = StringField(label='Yazar', validators=[Length(max=25), DataRequired()])
    submit = SubmitField(label='Submit',validators=[DataRequired()])

class SubscribeForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    submit = SubmitField(label='Submit', validators=[DataRequired()])
