import sqlite3
conn = sqlite3.connect('test.db')
print('Database connection openned!')
sql='''insert or replace into TourInfo (travel_agent, tour_id, tour_name, leave_date, 
        days, unfilled_places, total_places, fee) values (?, ?, ?, ?, ?, ?, ?, ?)'''
valueList = []
                
valueList.append(('Gloria','KS205CI8913A',\
 '【馬新旺福】馬新雙國吉隆坡高塔自助餐馬六甲5D立體藝術館金沙娛樂城超值五日遊(新加坡一晚)',\
                '2018/09/13', 5, 17, 18, 21588))        
conn.executemany(sql, valueList)    
conn.commit()