# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2018/12/25 14:54
import configparser

class ReadIni():

    def __init__(self,file_name=None,node=None):
        if file_name==None:
            file_name='C:\Ethan\MALL\config\LocalElement.ini'
        if node==None:
            self.node='LoginElement'
        else:
            self.node=node
        self.cf=self.load_ini(file_name)

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self,key):
        data=self.cf.get(self.node,key)
        return data



if __name__=='__main__':
    read=ReadIni()
    data=read.get_value('user_email')
    print(data)


