from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm,LoginForm

app= Flask(__name__)

app.config['SECRET_KEY']='ee4c4ee3cfac43d9d3df3bb4f9532b4b'

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
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('Home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def Login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data=='password':
            flash(f'You have been logged in!','success')
            return redirect(url_for('Home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)

