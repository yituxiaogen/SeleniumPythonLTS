# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2018/12/26 17:32

import os
import sys
sys.path.append('C:/Ethan/MALL')
import time
import unittest
from business.login_bussines import LoginBussines
from  log.user_log import  UserLog
from selenium import webdriver
class mall_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.userlog = UserLog()
        cls.log = cls.userlog.get_log()

    def setUp(self):
        self.dr =webdriver.Chrome()
        self.dr.get('http://47.88.50.127:8061/login')
        self.log.info("this is chrome")


    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                path=os.getcwd()[0:-5]
                file_path1=os.path.join(path , 'image',case_name+'.png')
                print(file_path1)
                self.dr.save_screenshot(file_path1)
        time.sleep(5)
        self.dr.quit()
    @classmethod
    def tearDownClass(cls):
        cls.userlog.close_handle()

    def test_log011(self):
        ##账号为真跳转建议更改密码
        data_massage=LoginBussines(self.dr).login('200@200.com','12345678')
        self.assertEqual(data_massage[0], 'None')
        self.assertEqual(data_massage[1], 'http://47.88.50.127:8061/console/password')
        self.assertEqual(data_massage[2], 'None')

    def test_log012(self):
        ##账号为真密码为假
        data_massage=LoginBussines(self.dr).login('200@200.com','123456789')
        self.assertEqual(data_massage[0], 'Password is wrong')
        self.assertEqual(data_massage[1], 'http://47.88.50.127:8061/login')
        self.assertEqual(data_massage[2], 'None')

    def test_log013(self):
        data_massage=LoginBussines(self.dr).login('20190198@20190198','123456789')
        self.assertEqual(data_massage[0], 'None')
        self.assertEqual(data_massage[1], 'http://47.88.50.127:8061/submitted/008699999999999')
        self.assertEqual(data_massage[2], 'Your application for LTS Mall new account is still in progress.')

    def test_log014(self):
        data_massage = LoginBussines(self.dr).login('20190199@20190199', '123456789')
        self.assertEqual(data_massage[0], 'None')
        self.assertEqual(data_massage[1], 'http://47.88.50.127:8061/refused/008699999999999')
        self.assertEqual(data_massage[2], 'Thank you for your interest in becoming an LTS dealer partner.')




if __name__ =="__main__":
    unittest.main()

    # file_path=os.path.join(os.getcwd()+"report"+"first_case.html")
    # print(file_path)
    # f=open(file_path,'wb')
    # suite=unittest.TestSuite()
    # suite.addTest(mall_login("test_log011"))
    # suite.addTest(mall_login("test_log012"))
    # runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title=" 登陆测试报告",description="hahahhahhaha")
    # runner.run(suite)

    # unittest.main()
    # path = str(os.getcwd())
    # path =path[0:-5]
    # print(path)
    # file_path1 = os.path.join(path, 'image','case_name .png')
    # print(file_path1)
