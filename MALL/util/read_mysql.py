# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/10 9:22

import pymysql
conn=pymysql.connect(
                    host='rj9iu3e27o7oxy110ao.mysql.rds.aliyuncs.com',
                     port=3306,
                     user='ltsb2b_app',
                     passwd='ltsb2b_app',
                     charset='utf8'
                     )
# con=conn.cursor()
# con.execute('')
# data=con.fetchall()
# print(data)