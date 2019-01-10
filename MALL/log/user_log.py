# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/8 15:34
import logging,time,os,datetime

class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  ###设置日志等级
        ####控制台输出日志
        # consle=logging.StreamHandler()
        # logger.addHandler(consle)
        # logger.debug()
        # ###文件名字
        now=datetime.datetime.now().strftime("%Y-%m-%d")
        base_dir=os.path.dirname(os.path.abspath(__file__))
        log_name=os.path.join(base_dir,'logs',now+"的日志.log")
        print(log_name)

        ###文件输出日志
        self.file_handle=logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        ###添加一些格式到file_handle
        formatter=logging.Formatter('%(asctime)s %(filename)s -->> %(funcName)s %(levelno)s: %(levelname)s --->> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        # self.logger.debug("hello world")


    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__=='__main__':
    log=UserLog()
    log1=log.get_log()
    log1.info('test')
    log.close_handle()










