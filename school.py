from flask import Flask
from flask.templating import _render, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
