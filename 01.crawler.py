#import unicodedata
#import urllib3
#from lxml.html import fromstring, tostring



import time
import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('npo_list.db')
print(conn)
for i in range(1482, 8310):
    ngo_index = i
    ngo_url = "http://npo.moi.gov.tw/npom/homepage/detail/26888" + str(ngo_index)
    value = [str(i), '', '', '', '', '']

    r = requests.get(ngo_url)
    r = BeautifulSoup(r.content, 'html.parser')
    ngo_table = r.find('table')
    
    print('index : ', i)
    x = 1
    sql_e = "'" + value[0] + "'"
    
    for j in ngo_table.find_all('tr'):
        value[x] = j.find_all('td')[1].string.strip()
        x = x + 1
    
    if value[5] == '' :
        value[5] = value[4]
        value[4] = '#'
        
    for j in range(1, 6):
        sql_e = sql_e + ', ' + "'" + value[j] + "'"
    
    sql_ex = "INSERT INTO TWNGO_LIST (ID, TYPE, NAME, ADDR, TELP, ADMR) VALUES ("+ sql_e + ");"
    
    conn.execute(sql_ex)
    
    if (i % 50 == 0):
        conn.commit()
        print(value)
        print('     ------------------')
        time.sleep(20)
        
conn.commit()
conn.close()
