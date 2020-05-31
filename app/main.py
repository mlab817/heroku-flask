from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return '<h1>Welcome to my first Heroku python Flask app!</h1>'