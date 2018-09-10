class GloriaCrawler():
    def __init__(self):
        print('init done.')
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
        html = resp.text
        #https://regex101.com/r/XHuNJH/1
        pattern = r'<div class=\"product_name\">.*?<span class=\"product_num\">[\d\w]+</span>\s*\r\n\s*(?P<TourName>.*?)\s*\r\n\s*<div class=\"product_tag\">.*?<div class=\"product_days\">(?P<Days>\d+)天.*?<div class=\"product_date normal\">(?P<Date>\d{4}/\d{2}/\d{2}).*?售價\$<strong>(?P<Money>[0-9,]+)</strong>.*?機位<\/span><span class=\"number\">(?P<Total>\d+)</span>.*?可售<\/span><span class=\"number\">(?P<Available>\d+)</span><\/div>'

        import re
        # DOTALL：就是csharp裡面的singleline
        pattern = re.compile(pattern, re.DOTALL)
        for m in pattern.finditer(html):
            print("TourName:" + m.group('TourName'))  
            print("Days:" +m.group('Days'))  
            print("Date:" +m.group('Date'))  
            print("Money:" +m.group('Money'))  
            print("Total:" +m.group('Total'))  
            print("Available:" +m.group('Available'))  

        #換頁
        #取得日期參數
        import pandas as pd
        #開始日期
        beginDt = pd.datetime.now().date()        
        beginDt = pd.datetime.now().date().strftime('%Y %m %d').replace(' ','%2F')
        #結束日期
        endDt = pd.datetime.now().date() + pd.DateOffset(months=6)                                
        #post_data = {'displayType':'G', 'orderCd':'1', 'pageALL':'2', 'pageGO':'1', 'pagePGO':'1', 'waitData':'false', 'waitPage':'false', 'beginDt':'2018%2F09%2F09', 'endDt':'2019%2F03%2F09', 'allowJoin':'1', 'allowWait':'1'}
        
        #page2
        post_data = {'displayType':'G', 'orderCd':'1', 'pageALL':'2', 'pageGO':'1', 'pagePGO':'1', 'waitData':'false', 'waitPage':'false', 'beginDt':beginDt, 'endDt':endDt, 'allowJoin':'1', 'allowWait':'1'}
        post_response = requests.post(url='https://www.gloriatour.com.tw/EW/Services/SearchListData.asp', data=post_data)
        html = post_response.text
        #剖析出html中的JSON               
        # pattern = r'.*?''(?P<value>\{.*?\})''.*?'
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
            # print(allToursJSON)
            # allToursJSONArray = json.load(allToursJSONString)
            for item in allToursJSONArray:
                print('-------------------------------')
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



        print('thread end.')
