from Crawlers import GloriaCrawler, OrangeCrawler
import threading
import time

objG = GloriaCrawler('Gloria', 'https://www.gloriatour.com.tw/EW/GO/GroupList.asp' \
, 'https://www.gloriatour.com.tw/EW/Services/SearchListData.asp' \
, 3)
# 建立一個子執行緒並立刻執行
t = threading.Thread(target = objG.Go())


objO = OrangeCrawler('Orange', 'http://www.orangetour.com.tw/EW/GO/GroupList.asp' \
, 'http://www.orangetour.com.tw/EW/Services/SearchListData.asp' \
, 3)
# 建立一個子執行緒並立刻執行
t1 = threading.Thread(target = objO.Go())

# 主執行緒繼續執行自己的工作
for i in range(10000):
  print("Main thread sleeping:", i)
  time.sleep(1)

print('program end')
