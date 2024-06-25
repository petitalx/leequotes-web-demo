from flask import Flask
from leequotes import leequotes

app = Flask(__name__)


@app.route('/')
def hello_world():
    return leequotes.random()

