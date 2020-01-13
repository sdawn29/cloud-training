import sqlite3
con = sqlite3.connect('Mydb.sqlite3')

# import pymysql
# con = pymysql.connect(user='', password='', host='', port='', database='')

cur = con.cursor()
query = '''CREATE TABLE IF NOT EXISTS logdata(
           ip VARCHAR(100),
           date VARCHAR(100),
           pics VARCHAR(100),
           url VARCHAR(100))'''
cur.execute(query)

import urllib.request as u
myurl = 'https://www.jafsoft.com/searchengines/log_sample.html'
f = u.urlopen(myurl)

import re
for line in f:
    # print(line)
    # print(type(line))
    line = line.decode()
    # print(type(line))
    m = re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-z]{3}/\d{4}).*(?:GET|POST)\s+/(?:pics/(\w+\.\w+))?.*(http://\S+)</A>.*', line)
    if m is not None:
        ip = m.group(1)
        dt = m.group(2)
        im = m.group(3)
        url = m.group(4)
        if im is None:
            im = 'No Image'
        # print(ip, dt, im, url)
        query = f"INSERT INTO logdata VALUES('{ip}', '{dt}', '{im}', '{url}')"
        # print(query)
        # cur.execute(query)

con.commit()
cur.execute('SELECT * FROM logdata')
result = cur.fetchall()
print('result =', result)

import csv
F = open('dbdump.csv', 'w', newline='')
wt = csv.writer(F)
wt.writerow(['IP', 'DATE', 'PICS', 'URL'])
for eachrow in result:
    wt.writerow(eachrow)
F.close()

F = open('dbdump.csv')
rdr = csv.reader(F)
csv_out = list(rdr)
print('csv_out =', csv_out)

'''
pandas
|
|-- Series for 1D data
|-- Dataframes for 2D data
'''

import pandas as pd
df1 = pd.DataFrame([[10, 20, 30], [40, 50, 60]], index=['r1', 'r2'], columns=['c1', 'c2', 'c3'])
print(df1)
L1 = list([[10, 20, 30], [40, 50, 60]])

df2 = pd.DataFrame(result)
print(df2)
df2.to_csv('out3.csv', index=None, header=['IP', 'DATE', 'PICS', 'URL'])

cur.execute('SELECT * FROM logdata')
df3 = pd.DataFrame(cur)
df3.to_csv('out4.csv', index=None, header=['IP', 'DATE', 'PICS', 'URL'])

df3.to_excel('out5.xlsx')
df4= df3.T
df4.to_json('out6.json')
