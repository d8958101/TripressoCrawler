#!/usr/bin/python
#D:\Projects\PythonWorkspace\TripressoCrawler\DBSchema\TableSchema\TourInfo.py
# 旅遊資訊資料表的table schema(SQLite)

import sqlite3

conn = sqlite3.connect('test.db')
print('Opened database successfully')
c = conn.cursor()
sql = ''' CREATE TABLE IF NOT EXISTS TourInfo (
                                    travel_agent text not null,
                                    tour_id text not null,
                                    tour_name text NOT NULL,
                                    leave_date text NOT NULL,                                    
                                    days integer NOT NULL,                                          
                                    unfilled_places integer NOT NULL,
                                    total_places integer NOT NULL,
                                    fee integer NOT NULL,
                                    PRIMARY KEY (travel_agent, tour_id)
                                ); '''

c.execute(sql)                                

print('Table TourInfo created successfully')
conn.commit()
conn.close()