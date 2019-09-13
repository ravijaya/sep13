import sqlite3

conn = sqlite3.connect('sep12.sqlite')
cur = conn.cursor()


def insert_rows(rows):
    query = 'insert into user (name, ugroup, email)  values (?, ?, ?)'
    cur.executemany(query, rows)
    conn.commit()


def create_table():
    query = """
    create table user(
    id integer primary key autoincrement,
    name varchar(32),
    ugroup varchar(32),
    email varchar(64))
    """

    cur.execute(query)


if __name__ == '__main__':
    # create_table()
    data = [['root', 'root', 'admin@localhost'],
            ['ravi', 'wheel', 'ravi@localost'],
            ['training', 'tarining,wheel', 'training@localhost']]
    insert_rows(data)

    cur.close()
    conn.close()
