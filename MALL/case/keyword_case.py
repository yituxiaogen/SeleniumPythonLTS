# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author:Ethan
# @Time: 2019/1/6 18:11
from MALL.util.read_excel import ReadExcel
from MALL.keywordselenium.actionMethod import ActionMethod
import sys,time
# sys.path.append()
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel=ReadExcel('C:\Ethan\MALL\config\login.xls')
        case_lines=handle_excel.get_lines()
        if case_lines:
            print(case_lines)
            for i in range(1,case_lines):
                handle_excel.write_value(i,15,'hello')
                time.sleep(1)
                is_run=handle_excel.get_col_value(i,3)
                # print(is_run)
                if is_run=='yes':
                    method= handle_excel.get_col_value(i, 4)
                    send_value=str(handle_excel.get_col_value(i, 5))
                    handle_value=handle_excel.get_col_value(i, 6)#####操作元素
                    except_result_method=handle_excel.get_col_value(i, 7)####预期结果使用方法
                    except_result=handle_excel.get_col_value(i, 8)###预期结果值
                    self.run_method(method,send_value,handle_value)
                    # print(send_value)

                    if except_result !='':
                        except_value=self.get_except_result_value(except_result)
                        if except_value[0]=='text':
                            result=self.run_method(except_result_method)
                            print(result)
                            if except_value[1] in result:
                                handle_excel.write_value(i,9,'pass')
                            else:
                                handle_excel.write_value(i,9,'fail')
                        elif except_value[0]=='element':
                            result=self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,9,'pass')
                            else:
                                handle_excel.write_value(i,9,'fail')
                        else:
                            print('没有else')
                    else:
                        print('预期结果为空')



        ##拿到行数
        ##循环行数，去执行每一行case
        ##是否执行
            ##拿到执行方法
            ##拿到操作值
            ##拿到输入数据
            ##是否有输入数据
                ##执行方法（输入数据，操作元素）
            ##没有输入数据
                ##执行方法（操作元素）
    ###获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,send_value='',handle_value=''):
        method_value=getattr(self.action_method,method)
        if send_value==''and handle_value !='':
            result=method_value(handle_value)
        elif handle_value != ''and send_value!='':
            result =method_value(send_value, handle_value)
        elif handle_value != ''and send_value=='':
            result =method_value(handle_value)
        else:
            result =method_value()
        return result

if __name__=='__main__':
    key=KeywordCase()
    key.run_main()

