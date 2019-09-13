from flask import Flask, render_template, request, jsonify
import sqlite3
from webdev.taskmodel import get_tasks, get_tasks_by_id, delete_task_by_id

app = Flask(__name__)


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = delete_task_by_id(task_id)
    return jsonify(dict(status='success'))


@app.route('/api/tasks', methods=['GET'])
def get_tasks_api():
    return jsonify(get_tasks())


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = get_tasks_by_id(task_id)
    return jsonify(dict(task=task))


@app.route('/formaction', methods=['POST'])
def add_task_action():
    # print(request.form)
    form = request.form
    query = 'insert into TASK (TITLE, DESCRIPTION, DONE) values ("{}", "{}", 0)'
    query = query.format(form['title'], form['desc'])

    with sqlite3.connect('../march27.sqlite') as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        task_id = cur.lastrowid

    return render_template('addtaskconfirm.html', task_id=task_id,
                           title=form['title'], desc=form['desc'],
                           flash=1)


@app.route('/addtask')
def add_task():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
