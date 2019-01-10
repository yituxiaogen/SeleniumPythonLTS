# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/4 18:05
import ddt
from selenium import webdriver
import unittest
from  MALL.business.login_bussines import LoginBussines
data=[['20190102@20190102', '123456789', 'None', 'http://47.88.50.127:8061/home', 'None', '账号密码为真'],
        ['20190102@20190102', '123456789', 'None', 'http://47.88.50.127:8061/home', 'None', '账号密码为真']]
@ddt.ddt   #####数据驱动
class DataaTest(unittest.TestCase):

    def setUp(self):
        # self.dr =webdriver.Chrome()
        # self.dr.get('http://47.88.50.127:8061/login')
        print("这是setup")

    def tearDown(self):
        print("这是teardown")
        # self.dr.quit()

    # @ddt.data(
    #     ['20190102@20190102', '123456789', 'None', 'http://47.88.50.127:8061/home', 'None', '账号密码为真'],
    #     ['20190102@20190102', '123456789', 'None', 'http://47.88.50.127:8061/home', 'None', '账号密码为真']
    # )
    @ddt.data(*data)

    # @ddt.unpack   ###解包
    def test_add(self,data):
        username, password, error, url, account_massage, describe=data
        print(username,password,error,url,account_massage,describe)
        data_massage=LoginBussines(self.dr).login(username,password)
        self.assertEqual(data_massage[0], error)
        self.assertEqual(data_massage[1], url)
        self.assertEqual(data_massage[2], account_massage)

if __name__=='__main__':
    unittest.main()