import MySQLdb
import requests

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "root", "graduationproject", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT ImageURLS FROM book_book;"

a = ""

# with open("test.txt","w") as f:
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()

   for row in results:
      # print(row[0])
      r = requests.get(row[0])
      if len(r.text) < 100:
         # f.write(row[0])
         sql2 = "UPDATE book_book SET ImageURLS =" + "'" + a + "'" +" WHERE ImageURLS = " + "'" + row[0] + "'"
         # sql2 = "UPDATE book.bx_books SET Image = 'h.jpg' WHERE Image = " + row[0]
         print(sql2)
         cursor.execute(sql2)
         # 提交到数据库执行
         db.commit()
      else:
         a = row[0]

except:
   print ("Error: unable to fetch data")

# 关闭数据库连接
db.close()