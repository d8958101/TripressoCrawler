def ExecSQLInsert(sql,values):
    import sqlite3
    conn = sqlite3.connect('test.db')
    print('Database connection openned!')
    cur = conn.cursor()
    cur.execute(sql,values)
    # if 'insert' in sql:
    #     v=('Gloria', 'SELA5OZ8914C' , \
    #     '【花漾韓國】∼入住首爾市區飯店+升等五花飯店∼韓服體驗、愛寶樂園、冰雪樂園、光明洞窟、拌飯秀５天', \
    #     '2018/09/14', 0, 20, 14500)
    #     cur.execute(sql,v)
    # else:
    #     cur.execute(sql)

    conn.commit()
    print('SQL Committed:' + sql)
    conn.close()
    print('Database connection closed!')



class TourInfo():
    def __init__(self, travelAgent, tourId, tourName, leaveDate, \
    days, unfilledPlaces, totalPlaces, fee):
        self.travelAgent = travelAgent
        self.tourId = tourId
        self.tourName = tourName
        self.leaveDate = leaveDate
        self.days = days
        self.unfilledPlaces = unfilledPlaces
        self.totalPlaces = totalPlaces
        self.fee = fee
        self.__sql='''insert into TourInfo (travel_agent, tour_id, tour_name, leave_date, 
        days, unfilled_places, total_places, fee) values (?, ?, ?, ?, ?, ?, ?, ?)'''
        self.__values =(travelAgent, tourId , tourName, leaveDate, days, unfilledPlaces,\
         totalPlaces, fee)
        
    def insertDb(self):
        ExecSQLInsert(self.__sql, self.__values)

        
# class SQLObj():
#     def __init__(self, sql, values):
#         self.sql = sql
#         self.values = values
