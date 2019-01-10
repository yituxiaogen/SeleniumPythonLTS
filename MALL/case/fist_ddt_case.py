# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/4 19:52
import sys,time,os,ddt,unittest
sys.path.append('C:/Ethan/MALL')
from selenium import webdriver
import HTMLTestRunnertest
from  business.login_bussines import LoginBussines
from util.read_excel import ReadExcel
data=ReadExcel().get_data()
# print(data)
@ddt.ddt
class DataaTest(unittest.TestCase):

    def setUp(self):
        self.dr =webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.get('http://47.88.50.127:8061/login')

    def tearDown(self):
        ###断言出错，当前页面截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                path=os.getcwd()[0:-5]
                file_path1=os.path.join(path , 'image',case_name[0:15]+'.png')
                self.dr.save_screenshot(file_path1)
        self.dr.quit()
    # @ddt.data(
    #     ['20190102@20190102', '12345678', 'None', 'http://47.88.50.127:8061/home', 'None', '账号密码为真'],
    # )'''
    # @ddt.unpack   ###解包
    @ddt.data(*data)
    def test_add(self, data):
        username,password,error,url,account_massage,describe = data
        data_massage=LoginBussines(self.dr).login(username,password)
        self.assertEqual(data_massage[0], error)
        self.assertEqual(data_massage[1], url)
        self.assertEqual(data_massage[2], account_massage)

if __name__ == '__main__':
    # unittest.main()
    now=time.strftime("%Y-%m-%d_%H-%M",time.localtime())
    path_path = os.path.dirname(os.path.abspath(__file__))[0:-5]
    file_path=os.path.join(path_path,"report",f"{now}执行的测试报告.html")
    print(file_path)
    f=open(file_path,'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(DataaTest)
    runner=HTMLTestRunnertest.HTMLTestRunner(stream=f,title=" 登陆测试报告",description="你好这是Ethan的测试报告")
    runner.run(suite)



