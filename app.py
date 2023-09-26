from flask import Flask

app = Flask(__name__)


@app.route('/')
def site():
    return 'hello word'


