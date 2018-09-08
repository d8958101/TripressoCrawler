from Crawlers import GloriaCrawler
#from Crawlers.GloriaCrawler import GloriaCrawler

import threading
import time

objG = GloriaCrawler()
# 建立一個子執行緒
t = threading.Thread(target = objG.Go())

# 執行該子執行緒
t.start()

# 主執行緒繼續執行自己的工作
for i in range(10):
  print("Main thread:", i)
  time.sleep(1)



print('program end')
