import sqlite3
conn = sqlite3.connect('test.db')
cur = conn.cursor()

for row in cur.execute('SELECT * FROM TourInfo'):
    print(row)

conn.close()