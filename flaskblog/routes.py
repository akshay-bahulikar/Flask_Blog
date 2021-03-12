from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

posts=[
    {
        'author' : 'Akshay Bahulikar',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'April 1, 2020', 
    },
    {
        'author' : 'Aditya Bahulikar',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'March 1, 2020', 
    }
]

@app.route("/")
def Home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def About():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def Register():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in','success')
        return redirect(url_for('Home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Home'))
        else:
            flash(f'Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def Logout():
    logout_user()
    return redirect(url_for('Home'))

@app.route("/account")
@login_required
def Account():
    return render_template('account.html', title='Account')
