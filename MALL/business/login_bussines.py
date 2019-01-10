# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2018/12/26 20:12
import os
import sys
sys.path.append('C:/Ethan/MALL')
from selenium import webdriver
from page.login_page import LoginPage
from  time import *

class LoginBussines(object):

    def __init__(self,dr):
        self.dr=dr
###登陆业务场景
    def login (self,useremail,password):
        data_massage=[]
        LoginPage(self.dr).login_send_useremail(useremail)
        sleep(1)
        LoginPage(self.dr).login_send_password(password)
        sleep(1)
        LoginPage(self.dr).login_click_sign_in()
        sleep(1.5)
        try:
            error=LoginPage(self.dr).login_print_error()
            data_massage.append(error)
        except:
            error='None'
            data_massage.append(error)
        sleep(1)
        url=self.dr.current_url
        data_massage.append(url)
        sleep(1)
        try:
            massage=LoginPage(self.dr).login_account_massage()
            data_massage.append(massage)
        except:
            massage="None"
            data_massage.append(massage)
        print(data_massage)
        sleep(1)

        return data_massage

if __name__=='__main__':
    dr = webdriver.Chrome()
    dr.get('http://47.88.50.127:8061/login')
    LoginBussines(dr).login('20190198@20190198',123456789)