from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard_wcookie/')
def dashboard_cookie():
    return render_template('dashboard_wcookie.html')

if __name__ == "__main__":
    app.run(debug=True)