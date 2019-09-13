import sqlite3

conn = sqlite3.connect('sep12.sqlite')
cur = conn.cursor()
cur.execute('select sqlite_version()')
print(cur.fetchone())
cur.close()
conn.close()