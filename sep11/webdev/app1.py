from flask import Flask, render_template
from time import ctime
from os import environ

app = Flask(__name__)


@app.route('/env')
def print_env():
    return render_template('env.html', environ=environ)


@app.route('/')
def home_page():
    return '<h1> a sample page</h1>'


@app.route('/ts')
def ts():
    return render_template('ts.html', current_ts=ctime())


if __name__ == '__main__':
    app.run(debug=True)
