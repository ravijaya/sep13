import sqlite3
from pprint import pprint as pp


def add_user_model(user_data):
    conn = sqlite3.connect('sep12.sqlite')
    cur = conn.cursor()
    query = 'insert into user (name, ugroup, email) values (?, ?, ?)'
    cur.execute(query, user_data)
    conn.commit()
    conn.close()
    return select_user_by_id(cur.lastrowid)


def select_user_by_id(user_id):
    conn = sqlite3.connect('sep12.sqlite')
    cur = conn.cursor()
    query = f'select * from user where id == {user_id}'
    cur.execute(query)
    column_header = [column_info[0] for column_info in cur.description]
    user = cur.fetchone()
    conn.close()
    return dict(zip(column_header, user))


def select_all_users():
    conn = sqlite3.connect('sep12.sqlite')
    cur = conn.cursor()

    query = 'select * from user;'
    cur.execute(query)
    column_header = [column_info[0] for column_info in cur.description]
    rows = cur.fetchall()
    conn.close()
    return [dict(zip(column_header, row)) for row in rows]


if __name__ == '__main__':
    print(add_user_model(['pam', 'bin', 'pam@map.com']))
    # select_all_users()
    # pp(select_all_users())
    # pp(select_user_by_id(3))
    # import itertools
    # print(dict(itertools.zip_longest(keys, values)))
