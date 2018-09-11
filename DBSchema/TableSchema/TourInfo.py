#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print('Opened database successfully')
c = conn.cursor()
c.execute('''CREATE TABLE TourInfo
       (Id TEXT  PRIMARY KEY NOT NULL,
       TourName       TEXT    NOT NULL,
       Days            INT     NOT NULL,
       Date           TEXT      NOT NULL,
       Total           INT      NOT NULL,
       Available       INT      NOT NULL,
       Money         INT     NOT NULL);''')
print('Table TourInfo created successfully')
conn.commit()
conn.close()