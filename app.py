# flask libraries
from flask import Flask, render_template, url_for, redirect, session, request
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

#system libraries
import os

# database related libraries 
import psycopg2
import urllib.parse
import uuid

app = Flask(__name__)
app.config['DEBUG'] = True

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
bootstrap.init_app(app)

@app.route('/')
def new_func():
    return render_template("index.html")

@app.route('/login')
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect('/message')
	return render_template("login.html", title="Sign In", form=form)

@app.route('/message', methods=['GET', 'POST'])
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
