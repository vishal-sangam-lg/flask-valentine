from flask import Flask, render_template

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/message/')
def about():
    return render_template('message.html')
