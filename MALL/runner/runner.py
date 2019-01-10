# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2018/12/28 22:20
import sys
sys.path.append('C:/Ethan/MALL')
import os,time
import HTMLTestRunnertest,selenium,unittest
from case.fist_ddt_case import DataaTest
###定义一个容器

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(DataaTest))
now=time.strftime("%Y-%m-%d_%H:%M",time.localtime())
print(now)
file_name=f"{now}点测试报告.html"
path_path=os.path.dirname(os.path.abspath(__file__))[0:-5]
# path_path='C:\Ethan\MALL'
path=os.path.join(path_path,'report',file_name)

print(path)
f=open(file_name,"wb")
runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title="LTS_Mall_测试报告",description=u"此处是描述")
runner.run(suite)
f.close()
print(path)
