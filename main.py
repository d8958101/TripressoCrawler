#D:\Projects\PythonWorkspace\TripressoCrawler\main.py
#主程式

from Crawlers import GloriaCrawler, OrangeCrawler
from concurrent.futures import ThreadPoolExecutor
import time

objG = GloriaCrawler('Gloria', 'https://www.gloriatour.com.tw/EW/GO/GroupList.asp' \
, 'https://www.gloriatour.com.tw/EW/Services/SearchListData.asp' \
, 3)

objO = OrangeCrawler('Orange', 'http://www.orangetour.com.tw/EW/GO/GroupList.asp' \
, 'http://www.orangetour.com.tw/EW/Services/SearchListData.asp' \
, 3)

#爬蟲類型網站很講求效能，因此使用multi-threading增加效能
with ThreadPoolExecutor() as executor:
    executor.submit(objG.Go())
    executor.submit(objO.Go())

# 主執行緒繼續執行自己的工作
# 避免主執行緒提早結束，影響到其他執行序
for i in range(10000):
  print("Main thread sleeping:", i)
  time.sleep(1)

print('program end')
