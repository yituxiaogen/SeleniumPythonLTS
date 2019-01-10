# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2018/12/25 17:51
import sys
sys.path.append('C:/Ethan/MALL')
from util.read_ini import ReadIni
class FindElement(object):
    def __init__(self,dr):
        self.dr=dr
    def get_element(self,key):
        read_ini= ReadIni()
        data=read_ini.get_value(key)
        by=data.split('>')[0]
        value=data.split('>')[1]
        try:
            if by == 'id':
                return self.dr.find_element_by_id(value)
            elif by == 'name':
                return self.dr.find_element_by_name(value)
            elif by == 'classname':
                return self.dr.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.dr.find_element_by_xpath(value)
        except:
            return None

    def get_element2(self):
        print('1')


if __name__=="__main__":
    pass


