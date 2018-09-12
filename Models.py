import sqlite3

def ExecSQLInsert(sql,values):    
    conn = sqlite3.connect('test.db')
    print('Database connection openned!')
    cur = conn.cursor()
    try:
        cur.execute(sql,values)  
        conn.commit()
        print('SQL Committed:' + sql)
    except:
        conn.rollback()
        print('SQL rollbacked::' + sql)
    
    conn.close()
    print('Database connection closed!')

class BulkInsert():
    def __init__(self):
        self.__sql = ''
        self.__valuesList = []

    def AddStatements(self, sql, values):        
        self.__sql = sql
        self.__valuesList.append(values)

    def execAndCommit(self):        
        conn = sqlite3.connect('test.db')
        print('Database connection openned!') 
        try:       
            conn.executemany(self.__sql, self.__valuesList)                
            conn.commit()
            print('SQL Committed:' + self.__sql)
        except:
            conn.rollback()
            print('SQL rollbacked::' + self.__sql)
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
        self.sql='''insert or replace into TourInfo (travel_agent, tour_id, tour_name, leave_date, 
        days, unfilled_places, total_places, fee) values (?, ?, ?, ?, ?, ?, ?, ?)'''
        self.values =(travelAgent, tourId , tourName, leaveDate, days, unfilledPlaces,\
         totalPlaces, fee)
                
    def deletedOldData(self, trueOrFalse):
        #是否刪除舊資料
        if trueOrFalse == False:
            self.sql = self.sql.replace('insert or replace','insert')    

    def insertDb(self):
        ExecSQLInsert(self.sql, self.values)

