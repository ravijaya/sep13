import sqlite3
from pprint import pprint as pp


def delete_task_by_id(task_id):
    query = 'delete from TASK where ID={}'.format(task_id)

    with sqlite3.connect('../march27.sqlite') as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()


def get_tasks_by_id(task_id):
    """list all available task"""
    query = 'select * from TASK where ID={}'.format(task_id)

    with sqlite3.connect('../march27.sqlite') as conn:
        cur = conn.cursor()
        cur.execute(query)
        # print(cur.description
        column_headings = [item[0] for item in cur.description]

        return [dict(zip(column_headings, row)) for row in cur.fetchall()]


def get_tasks():
    """list all available task"""
    query = 'select * from TASK'

    with sqlite3.connect('../march27.sqlite') as conn:
        cur = conn.cursor()
        cur.execute(query)
        # print(cur.description
        column_headings = [item[0] for item in cur.description]

        return [dict(zip(column_headings, row)) for row in cur.fetchall()]


if __name__ == '__main__':
    tasks = get_tasks()
    pp(tasks)
