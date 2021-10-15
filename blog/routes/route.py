from os import error
from flask import render_template, url_for, redirect, flash, session, request
from flask_login import login_user, logout_user, login_required
from blog import app, db, mail
from blog.forms.forms import RegisterForm, LoginForm, PostCreateForm, SubscribeForm
from blog.models.models import Member, Post
from flask_login.mixins import UserMixin
from flask_mail import Message
from sqlalchemy.exc import IntegrityError

@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(401)
def error_401(error):
    return render_template('errors/401.html'), 401


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500


@app.route('/')
def home_page():
    return render_template('pages/home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()

    if form.validate_on_submit():

        try:
            new_member = Member(form.username.data,
                                form.email.data, form.password.data)
            db.session.add(new_member)
            db.session.commit()
            flash(
            f'Registered successfuly. Welcome dear {new_member.username}.', category='register_ok')
            return redirect(url_for('home_page'))

        except IntegrityError:
            flash(message='Username/email is already used' , category='register_no')
            return redirect(url_for('register_page'))

    return render_template('pages/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():

    form = LoginForm()

    if form.validate_on_submit():

        deneme_kullanıcı = Member.query.filter_by(
            username=form.username.data).first()

        try:
            if deneme_kullanıcı.check_password(form.password.data):
                login_user(deneme_kullanıcı)
                flash(
                    message=f'Logged in successfuly! Welcome {deneme_kullanıcı.username}', category='login_ok')
                session["username"] = request.form["username"]
                return redirect(url_for('logged_page', username=session["username"]))
            else:
                flash(message=f"Wrong password!", category='login_bad')

        except AttributeError:
            flash(message=f"This member didn't exist!", category='login_bad')
            return redirect(url_for('login_page'))

    return render_template('pages/login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash(message=f'Logged out successfully!!', category='logout_ok')
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
        form.title.data = ""
        form.content.data = ""
        flash(message='Post created successfully!', category='post_ok')
        return redirect(url_for('logged_page', username=username))
    if form.errors != {}:
        for message in form.errors.values():
            flash(
                message=f'Somethings gone wrong :( : {message} !', category='post_bad')

    return render_template('pages/post_create.html', form=form)


@app.route('/<username>/post/delete <post_title>', methods=['GET', 'POST'])
def delete_post_page(username, post_title):
    try:
        delete_post = Post.query.filter_by(title=post_title).first()
        db.session.delete(delete_post)
        db.session.commit()
        flash('Writing deleted!', category='post_deleted')
        return redirect(url_for('logged_page', username=username))

    except Exception as error:
        raise error


@app.route('/<username>/post/change <_post_id>' , methods=['GET', 'POST'])
def change_post_page(username , _post_id):
    variables={}
    
    form = PostCreateForm()
    variables['form'] = form

    selected_post = Post.query.get(_post_id)
    
    variables['title'] = selected_post.title
    variables['content'] = selected_post.content

    if form.validate_on_submit():
        try:
            selected_post.title = form.title.data
            selected_post.content = form.content.data
            selected_post.author = username
            
            db.session.add(selected_post)
            db.session.commit()
            flash('Writing changed!', category='post_changed')

            return(redirect(url_for('logged_page' , username=username)))
        
        except Exception as error:
            raise error

    return render_template('pages/post_change.html' , variables=variables)

@app.route('/<username>/profile', methods=['GET', 'POST'])
@login_required
def logged_page(username):

    posts = Post.query.filter_by(author=username)
    posts = list(posts)

    post_num = len(posts)

    form = SubscribeForm()

    if form.validate_on_submit():
        msg = Message('Subscription!', recipients=[form.email.data])
        msg.body = 'Thanks for the mail subscription :)'
        mail.send(msg)
        flash(message=f'Mail sent successfully!!!', category='mail_ok')
        return redirect(url_for('logged_page'))

    return render_template('pages/logged.html', form=form, posts=posts, post_num=post_num)

@app.route('/social' , methods=['GET'])
@login_required
def social_page():
    
    return render_template('pages/social.html')