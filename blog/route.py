from flask import render_template, url_for, redirect, flash, session, request
from flask_login import login_user, logout_user, login_required
from blog import app, db, mail
from blog.forms import RegisterForm, LoginForm, PostCreateForm, SubscribeForm
from blog.models import Member, Post
from flask_login.mixins import UserMixin
from flask_mail import Message

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()

    if form.validate_on_submit():

        new_member = Member(form.username.data, form.email.data, form.password.data)
        db.session.add(new_member)
        db.session.commit()

        flash(f'Başarıyla kayıt olundu. Aramıza hoşgeldin {new_member.username}.', category='register_ok')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for message in form.errors.values():
            flash(f'Kayıt olunurken hata oluştu: {message} !', category='register_no')

    return render_template('register.html',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():

    form = LoginForm()

    if form.validate_on_submit():

        deneme_kullanıcı = Member.query.filter_by(username = form.username.data).first()

        if deneme_kullanıcı.check_password(form.password.data):
            login_user(deneme_kullanıcı)
            flash(message=f'Logged in successfuly! Welcome {deneme_kullanıcı.username}',category='login_ok')
            session["username"] = request.form["username"]
            return redirect(url_for('logged_page'))
        else:
            flash(message='Somethings gone wrong!',category='login_bad')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Başarıyla çıkış yaptınız.', category='logout_ok')
    return redirect(url_for('home_page'))

'''
    buradaki <username> base.html den geliyor, url_for fonksiyonunda parametre olarak
'''
@app.route('/<username>/post_create', methods=['GET', 'POST'])
@login_required
def post_create(username):
    form = PostCreateForm()

    if form.validate_on_submit():
        new_post = Post(form.title.data, form.content.data, form.author.data)
        db.session.add(new_post)
        db.session.commit()
        flash(message='Gönderi başarıyla oluşturuldu!', category='post_ok')
    if form.errors != {}:
        for message in form.errors.values():
            flash(f'Gönderi oluşturulurken hata oluştu :( : {message} !', category='post_bad')

    return render_template('post_create.html', form=form)


@app.route('/logged', methods=['GET','POST'])
@login_required
def logged_page():
    form = SubscribeForm()

    if form.validate_on_submit():
        msg = Message('Üyelik!', recipients=[form.email.data])
        msg.body='Mail üyeliğiniz tamamlandıııııı'
        mail.send(msg)
        flash('Mail başarıyla gönderildi!!!', category='mail_ok')
        return redirect(url_for('home_page'))


    return render_template('logged.html', form = form)
