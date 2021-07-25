from flask import Flask, render_template, url_for, request
from flask_pymongo import PyMongo
from forms import SignUpForm
from variables import *


app = Flask(__name__)

app.config['SECRET_KEY'] = 'hardsecretkey'
app.config['MONGO_URI'] = MONGO_URI

mongo = PyMongo(app)

user_collection = mongo.db.users

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup/', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        return 'Signed up!'
    return render_template('signup.html', form=form)

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard_wcookie/')
def dashboard_wcookie():
    return render_template('dashboard_wcookie.html')

if __name__ == "__main__":
    app.run(debug=True)