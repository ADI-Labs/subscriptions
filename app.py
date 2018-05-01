# flask libraries
from flask import Flask, render_template, url_for, redirect, session, request
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required
from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

#system libraries
import os

# database related libraries 
import psycopg2
import urllib.parse
import uuid

app = Flask(__name__)
app.config.update(dict(
	DEBUG = True,
	SECRET_KEY='powerful secretkey',
	WTF_CSRF_SECRET_KEY='a csrf secret key'
))

login_manager = LoginManager()
login_manager.init_app(app)

bootstrap = Bootstrap()
bootstrap.init_app(app)

# validators 
# post request - hash password, built-in feature
# insert those in database
# make sure validators are not blank


class LoginForm(Form):
	username = StringField('Username', [validators.Required()])
	password = PasswordField('Password', [validators.Required()])

@app.route('/')
def new_func():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():

		# username = request.form['username']
		# password = request.form['password']
		# check if actually work
		return redirect('new_func')
	return render_template('login.html', form=form)

@app.route('/settings')
@login_required
def settings():
	pass

@app.route('/logout')
@login_required
def logout():
	logout_user()
	# return redirect(url_for('login'))
	return render_template("login.html")

@app.route('/message', methods=['GET', 'POST'])
@login_required
def message():
    
    if request.method == 'POST':
        message = request.form['userInput']
#--->handle message to db query here        
        
    
    return render_template("message.html")




# database
urllib.parse.uses_netloc.append("postgres")
url = urllib.parse.urlparse(os.environ['postgres://rebtvlwibhdvwf:4d7f99eef7c8028b3fd6'
	+'303a08f43986eed2368acb84ecf84f323cb77491cba4@ec2-54-163-234-20.compute-1.amazonaws.com:5432/dc4m6ge7e3ahn6'])

conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
cur = conn.cursor()

if __name__ == "__main__":
	app.run()

# build user mixin class flask
# sql alchemy
# checking , query database for username, check if fails
# how to keep user logged in, password security

# query database directly
# ORM - allows you to map python objet to databse format

# resources: sql alchemy, allows you to define user class
# don't have to query database
# user table in database
# define sql alchemy class today

# flask textbook
# chapter 8: user authentication, user model
