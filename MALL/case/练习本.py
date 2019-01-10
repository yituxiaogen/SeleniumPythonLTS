# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/7 15:34
from selenium import webdriver
# from MALL.base.find_element import FindElement
import os,time
# import time,xlrd
#
# with  xlrd.open_workbook('C:\Ethan\MALL\config\login.xls', 'rb') as data:
#    table = data.sheets()[0]

# dr=webdriver.Chrome()
# dr.get('http://47.88.50.127:8061/login')
# print(dr.title)
# print(os.getcwd())
# now=time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime())
# print(now)
# dr=webdriver.Chrome()
# time.sleep(1)
# dr.get('https://www.baidu.com/')
base_dir=os.path.dirname(os.path.abspath(__file__))[0:-5]
print(base_dir)

