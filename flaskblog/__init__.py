from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SECRET_KEY']='ee4c4ee3cfac43d9d3df3bb4f9532b4b'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)

from flaskblog import routes