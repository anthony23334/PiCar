from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/auto')
def auto():
    return render_template('auto.html') 