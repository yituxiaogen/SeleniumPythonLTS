# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2018/12/26 17:04
import os
import sys
sys.path.append('C:/Ethan/MALL')
from base.find_element import FindElement

class LoginPage(object):

    def __init__(self,dr):
        self.findelement=FindElement(dr)

    def login_send_useremail(self,useremail):
        self.findelement.get_element('user_email').send_keys(useremail)

    def login_send_password(self,password):
        self.findelement.get_element('password').send_keys(password)

    def login_click_sign_in(self):
        self.findelement.get_element('sign_in').click()

    def login_click_forgot_password(self):
        self.findelement.get_element('password').click()

    def login_click_sign_up(self):
        self.findelement.get_element('sign_up').click()

    def login_clear_useremail(self):
        self.findelement.get_element('user_email').clear()

    def login_clear_password(self):
        self.findelement.get_element('password').clear()

    def login_print_error(self):
        error=self.findelement.get_element('error_massage').text
        return error

    def login_account_massage(self):
        massage=self.findelement.get_element('login_account_massage').text
        return massage





