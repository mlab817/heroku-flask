from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return '<h1>Welcome Home!</h1>'