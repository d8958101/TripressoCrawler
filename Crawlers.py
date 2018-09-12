class GloriaCrawler():
    def __init__(self):
        print('init done.')

    def GetPageData(self, rs,  pageNo):
        #取得日期參數
        import pandas as pd
        #開始日期
        beginDt = pd.datetime.now().date()        
        beginDt = pd.datetime.now().date().strftime('%Y %m %d').replace(' ','%2F')
        #結束日期
        endDt = pd.datetime.now().date() + pd.DateOffset(months=6)           
        post_data = {'displayType':'G', 'orderCd':'1', 'pageALL':pageNo, 'pageGO':'1', 'pagePGO':'1', 'waitData':'false', 'waitPage':'false', 'beginDt':beginDt, 'endDt':endDt, 'allowJoin':'1', 'allowWait':'1'}
        post_response = rs.post(url='https://www.gloriatour.com.tw/EW/Services/SearchListData.asp', data=post_data)
        html = post_response.text
        #剖析出html中的JSON               
        import re
        pattern = r'.*?''(?P<value>\{.*?"ErrMsg":.*?\})''.*?'
        # DOTALL：就是csharp裡面的singleline
        pattern = re.compile(pattern, re.DOTALL)        
        match = pattern.match(html)        
        if match:
            # 得到匹配結果
            # print(match.group('value'))
            import json
            jsonString = match.group('value')            
            jsonObj = json.loads(jsonString)
            allToursJSONArray  = jsonObj['All']

            from Models import BulkInsert
            bulkInsert = BulkInsert()
            for item in allToursJSONArray:
                print('-------------------------------')                
                #ProductNum                
                print("GrupCd:" + item['GrupCd'])
                #TourName                
                print("GrupSnm:" + item['GrupSnm'])
                #Date
                print("LeavDt:" + item['LeavDt'])
                #Available
                print("SaleYqt:" + str(item['SaleYqt']))
                #Total
                print("EstmTotqt:" + str(item['EstmTotqt']))
                #Monty
                print("SaleAm:" + str(item['SaleAm']))
                #Days
                print("天數GrupLn:" + str(item['GrupLn']))
                #url
                print("ShareUrl:" + item['ShareUrl'])
                print('-------------------------------')
                
                from Models import TourInfo
                tourInfo = TourInfo('Gloria', item['GrupCd'], item['GrupSnm'],\
                item['LeavDt'], item['GrupLn'], item['SaleYqt'], item['EstmTotqt'], \
                item['SaleAm'])
                bulkInsert.AddStatements(tourInfo.sql, tourInfo.values)
            
            bulkInsert.execAndCommit()    

    def Go(self):
                
        # 引入 requests 模組
        import requests
        #保留session
        rs = requests.session()
        resp = rs.get('https://www.gloriatour.com.tw/EW/GO/GroupList.asp')

        if resp.status_code == requests.codes.ok:
            print("OK")
        else:
            print("There is a problem!")
            exit()
                                                                   
        #爬page 1~3的資料
        for i in range(1,4):
            self.GetPageData(rs, i)
                    
        print('thread end.')

    
