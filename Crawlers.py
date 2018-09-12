# D:\Projects\PythonWorkspace\TripressoCrawler\Crawlers.py
# 定義爬蟲的class

#Base爬蟲，之後會直接給華泰爬蟲以及澄果爬蟲繼承
class BaseCrawler():
    def __init__(self, companyId, firstUrl, postUrl, totalPages):        
        self.companyId = companyId #這個同業的公司代碼
        self.firstUrl = firstUrl #透過get此網址，以取得合法的session
        self.postUrl = postUrl #透過post此網址，取得合法的JSON資料
        self.totalPages = totalPages #希望能爬該同業網站的幾個頁面
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
        post_response = rs.post(url=self.postUrl, data=post_data)
        html = post_response.text
        #以正規運算式剖析出html中的JSON資料               
        import re
        pattern = r'.*?''(?P<value>\{.*?"ErrMsg":.*?\})''.*?'        
        pattern = re.compile(pattern, re.DOTALL)        
        match = pattern.match(html)        
        if match:
            # 得到匹配結果
            # print(match.group('value'))

            #開始解析JSON裡面的旅遊資料
            import json
            jsonString = match.group('value')            
            jsonObj = json.loads(jsonString)
            allToursJSONArray  = jsonObj['All']

            from Models import BulkInsert
            
            #透過Bulk Insert降低存取db的時間
            bulkInsert = BulkInsert()
            for item in allToursJSONArray:
                # print('-------------------------------')                
                # #ProductNum                
                # print("GrupCd:" + item['GrupCd'])
                # #TourName                
                # print("GrupSnm:" + item['GrupSnm'])
                # #Date
                # print("LeavDt:" + item['LeavDt'])
                # #Available
                # print("SaleYqt:" + str(item['SaleYqt']))
                # #Total
                # print("EstmTotqt:" + str(item['EstmTotqt']))
                # #Monty
                # print("SaleAm:" + str(item['SaleAm']))
                # #Days
                # print("天數GrupLn:" + str(item['GrupLn']))
                # #url
                # print("ShareUrl:" + item['ShareUrl'])
                # print('-------------------------------')
                
                from Models import TourInfo
                tourInfo = TourInfo(self.companyId, item['GrupCd'], item['GrupSnm'],\
                item['LeavDt'], item['GrupLn'], item['SaleYqt'], item['EstmTotqt'], \
                item['SaleAm'])

                #透過TourInfo類別以及BulkInsert類別的搭配
                #能達到輕鬆執行BulkInsert的效果，無須再自行組SQL
                bulkInsert.AddStatements(tourInfo.sql, tourInfo.values)
            
            bulkInsert.execAndCommit()    

    def Go(self):
        #開始爬旅遊資料
        
        import requests       
        #先透過get(self.firstUrl)以取得合法的session資料
        rs = requests.session()
        resp = rs.get(self.firstUrl)

        if resp.status_code == requests.codes.ok:
            print("OK")
        else:
            print("There is a problem!")
            exit()
                                                                   
        #爬page 1~3的資料
        for i in range(1,self.totalPages+1):
            self.GetPageData(rs, i)
                    
        print('thread end.')

#華泰爬蟲
#直接繼承Base爬蟲即可
#未來若是華泰的網站架構變了，
#再override Base爬蟲的整個function即可
#或是再建立Lambda Function機制也可達到override 部分Base爬蟲的function的效果
class GloriaCrawler(BaseCrawler):
    def __init__(self, companyId, firstUrl, postUrl, totalPages):
        super().__init__(companyId, firstUrl, postUrl, totalPages)

#澄果爬蟲
#註解同上面的華泰爬蟲
class OrangeCrawler(BaseCrawler):
    def __init__(self, companyId, firstUrl, postUrl, totalPages):
        super().__init__(companyId, firstUrl, postUrl, totalPages)

