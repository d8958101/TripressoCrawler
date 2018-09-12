#D:\Projects\PythonWorkspace\TripressoCrawler\DBSchema\ExecSQL.py
#執行測試用的指令

import sqlite3
conn = sqlite3.connect('test.db')
print('Database connection openned!')
cur = conn.cursor()


sql = ''
# sql = 'delete  from TourInfo '
# sql = 'drop table TourInfo'
# sql='''insert into TourInfo (travel_agent, tour_id, tour_name, leave_date, 
# days, unfilled_places, total_places, fee) values (?, ?, ?, ?, ?, ?, ?, ?)'''
# sql = ''' CREATE TABLE IF NOT EXISTS TourInfo (
#                                     travel_agent text not null,
#                                     tour_id text not null,
#                                     tour_name text NOT NULL,
#                                     leave_date text NOT NULL,                                    
#                                     days integer NOT NULL,                                          
#                                     unfilled_places integer NOT NULL,
#                                     total_places integer NOT NULL,
#                                     fee integer NOT NULL,
#                                     PRIMARY KEY (travel_agent, tour_id)
#                                 ); '''



if 'insert' in sql:
    values=('Gloria', 'SELA5OZ8914C' , \
    '【花漾韓國】∼入住首爾市區飯店+升等五花飯店∼韓服體驗、愛寶樂園、冰雪樂園、光明洞窟、拌飯秀５天', \
    '2018/09/14', 5, 0, 20, 14500)
    cur.execute(sql,values)
else:
    cur.execute(sql)

conn.commit()
print('SQL Committed:' + sql)
conn.close()
print('Database connection closed!')