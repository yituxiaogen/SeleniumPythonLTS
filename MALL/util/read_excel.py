# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/5 19:38
import xlrd,os
from xlutils.copy import copy

class ReadExcel():
    def __init__(self,excil_path=None,index=None):
        if excil_path==None:
            path=os.path.join('C:\Ethan\MALL','config','login_case_data.xls')
            # print(os.getcwd()[0:-5])
            self.excel_path=path
            # print(excil_path)
        else:
            self.excel_path=excil_path
        if index==None:
            index=0
        with  xlrd.open_workbook(self.excel_path,'rb') as self.data:
            self.table=self.data.sheets()[index]
    def get_data(self):
        result=[]
        rows=self.get_lines()
        if rows != None:
            for i in range(1,self.get_lines()):
                col=self.table.row_values(i)
                result.append(col)
            return result
        return None
    ###获取Excel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None
    ###获取Excel单元格数据
    def get_col_value(self,row,col):
        if self.get_lines() > row:
            data=self.table.cell(row,col).value
            return data
        return None
    ###写入数据
    def write_value(self,row,col,value):
        with xlrd.open_workbook(self.excel_path,'rb') as read_value:
            write_data=copy(read_value)
            write_data.get_sheet(0).write(row,col,value)
            write_data.save(self.excel_path)

if __name__=="__main__":
    ex=ReadExcel()
    data=ex.get_data()
    print(data)