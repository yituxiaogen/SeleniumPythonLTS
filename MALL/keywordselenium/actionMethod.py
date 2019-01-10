# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/6 17:50
from selenium import webdriver
from MALL.base.find_element import FindElement
import time
class ActionMethod:
    def __init__(self):
        pass
    ###打开浏览器
    def open_browser(self,browser):
        if browser=="chrome":
            self.dr=webdriver.Chrome()
        elif browser=="firefox":
            self.dr=webdriver.Firefox()
        else:
            self.dr=webdriver.Edge()
    ##输入地址
    def get_url(self,url):
        self.dr.get(url)
    ###定位元素
    def get_element(self,key):
        find_element=FindElement(self.dr)
        element=find_element.get_element(key)
        return element
    ##输入元素
    def send_value(self,value,key):
        element=self.get_element(key)
        element.send_keys(value)
    ###点击元素
    def click_element(self,key):
        element=self.get_element(key)
        element.click()
    ###等待时间
    def sleep_time(self):
        time.sleep(1)
    ###关闭浏览器
    def close_browser(self ):
        self.dr.quit()
    ###获取title
    def get_title(self):
        return self.dr.title
