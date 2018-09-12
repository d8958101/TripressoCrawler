#D:\Projects\PythonWorkspace\TripressoCrawler\Models.py
#將程式邏輯與資料操縱邏輯分離，在此定義db資料操作相關的class以及method
#便於未來擴充以及維護

import sqlite3

#少量資料insert時使用的SQLInsert
def ExecSQLInsert(sql,values):    
    conn = sqlite3.connect('test.db')
    print('Database connection openned!')
    cur = conn.cursor()
    try:       
        # commit外面包一層try catch防止存取db時出現異常
        cur.execute(sql,values)  
        conn.commit()
        print('SQL Committed:' + sql)
    except:
        #萬一寫入db失敗時，執行rollback()
        conn.rollback()
        print('SQL rollbacked::' + sql)
    
    conn.close()
    print('Database connection closed!')

#大量資料寫入時，使用BulkInsert
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
            #使用executemany()而非execute()以降低存取db的次數     
            conn.executemany(self.__sql, self.__valuesList)                
            conn.commit()
            print('SQL Committed:' + self.__sql)
        except:
            conn.rollback()
            print('SQL rollbacked::' + self.__sql)
        conn.close()
        print('Database connection closed!')    


# 抓下來的旅遊資訊的class:
# 將旅遊資訊物件化，未來有類似的需求，後續的人便不用再麻煩的組SQL
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
        #爬到的旅行資料以最新的為主
        if trueOrFalse == False:
            self.sql = self.sql.replace('insert or replace','insert')    

    def insertDb(self):
        ExecSQLInsert(self.sql, self.values)

