class GloriaCrawler():
    def __init__(self):
        print('init done.')
    def Go(self):
                
        # 引入 requests 模組
        import requests
        # 使用 GET 方式下載普通網頁
        resp = requests.get('https://www.gloriatour.com.tw/EW/GO/GroupList.asp')

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
