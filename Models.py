import sqlite3

def ExecSQLInsert(sql,values):    
    conn = sqlite3.connect('test.db')
    print('Database connection openned!')
    cur = conn.cursor()
    cur.execute(sql,values)  
    conn.commit()
    print('SQL Committed:' + sql)
    conn.close()
    print('Database connection closed!')

class BulkInsertExecutor():
    def __init__(self):
        # self.__sql = ''
        # self.__valuesList = []
        pass
    # def AddStatements(sql, values):        
    #     self.__sql = sql
    #     self.__valuesList.append(values)

    # def SetSQL(sql):
    #     if self.sql <> '':
    #         self.__sql = sql.replace('?','%s')        

    def execAndCommit(self,sql,valueList):        
        conn = sqlite3.connect('test.db')
        print('Database connection openned!')
        #sql = sql.replace('?','%s')  
        conn.executemany(sql, valueList)    
        print('SQL Committed:' + sql)
        conn.commit()
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
                
    def deletedOldData(trueOrFalse):
        #是否刪除舊資料
        if trueOrFalse == False:
            self.sql = self.sql.replace('insert or replace','insert')    

    def insertDb(self):
        ExecSQLInsert(self.sql, self.values)

        
# class SQLObj():
#     def __init__(self, sql, values):
#         self.sql = sql
#         self.values = values
