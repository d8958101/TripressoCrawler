#D:\Projects\PythonWorkspace\TripressoCrawler\DBSchema\Query.py
#查詢抓下來的旅遊資訊

import sqlite3
conn = sqlite3.connect('test.db')
cur = conn.cursor()

for row in cur.execute('SELECT * FROM TourInfo'):
    print(row)

conn.close()