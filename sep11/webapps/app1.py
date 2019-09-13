from flask import Flask, render_template, request
from time import ctime
from os import environ
from subprocess import check_output

app = Flask(__name__)


@app.route('/compute', methods=['POST'])
def compute():
    # op = check_output(["grep", request.form["value1"], request.form["value2"]]).decode()
    return request.form["value1"] + request.form["value2"]
    # return f'<pre>{op}</pre>'


@app.route('/')
def index():
    return """<form action="/compute" method="post">
                value1 : <input type='text' name='value1'><br />
                value2 : <input type='text' name='value2'><br />
                <input type="submit" value="click"/></form>"""


@app.route('/env')
def get_env():
    return render_template('env.html', envvars=environ.items(), ts=ctime())


@app.route('/grepme')
def grep_me():
    # http://127.0.0.1:5000/grepme?pattern=root&filename=/etc/passwd
    pattern = request.args.get('pattern')
    file_name = request.args.get('filename')
    op = check_output(['grep', pattern, file_name]).decode()
    return f'<pre>{op}</pre>'


if __name__ == '__main__':  # main()
    app.run(debug=True)
