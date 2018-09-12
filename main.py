from Crawlers import GloriaCrawler, OrangeCrawler
from concurrent.futures import ThreadPoolExecutor
import time

objG = GloriaCrawler('Gloria', 'https://www.gloriatour.com.tw/EW/GO/GroupList.asp' \
, 'https://www.gloriatour.com.tw/EW/Services/SearchListData.asp' \
, 3)

objO = OrangeCrawler('Orange', 'http://www.orangetour.com.tw/EW/GO/GroupList.asp' \
, 'http://www.orangetour.com.tw/EW/Services/SearchListData.asp' \
, 3)

with ThreadPoolExecutor() as executor:
    executor.submit(objG.Go())
    executor.submit(objO.Go())

# 主執行緒繼續執行自己的工作
for i in range(10000):
  print("Main thread sleeping:", i)
  time.sleep(1)

print('program end')
