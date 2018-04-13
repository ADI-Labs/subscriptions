from flask import Flask, render_template, url_for, redirect, session, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['DEBUG'] = True

bootstrap = Bootstrap()
bootstrap.init_app(app)

@app.route('/')
def new_func():
    return render_template("index.html")

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/message', methods=['GET', 'POST'])
def message():
	return render_template("message.html")

if __name__ == "__main__":
	app.run()