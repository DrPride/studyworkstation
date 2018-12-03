# -*- coding:utf-8 -*- 
# analyze the content of the form
import xlrd
import csv
import os
import database as db
import title_analyze as ta

class file_analyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.open_file()

    def open_file(self):
        # 打开文件夹获取第一张表
        book = xlrd.open_workbook(self.file_name)
        table = book.sheets()[0]
        self.table = table
        return table

    # 寻找含有列名的那一行
    # object_name = table.row_values(0) 这个直接获取了第一行的值
    def get_object(self):
        for i in range(5):
            object_name = self.table.row_values(i)
            str_list = str(object_name)
            if str_list.find('学号') or str_list.find('姓名'):
                return object_name




if __name__ == '__main__':
    #main()
    file_analyzer1 =  file_analyzer('data/6月勤工助学工资-发银行.xlsx')
    print(file_analyzer1.get_object())