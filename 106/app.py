import os 
from flask import Flask
from markupsafe import escape

os.system('cls' if os.name == 'nt' else 'clear')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/hello/<name>")
def hello(name):
    #  http://127.0.0.1:5000/hello/Simoes
    return f"<p>Hello, {escape(name)}!</p>"