# -*- coding: utf-8 -*-
import xlrd
import csv
import os
import database as db

filename = 'data/2018年国家奖助学金发放表10.29.xlsx'
xlrd.Book.encoding = "utf-8"
book = xlrd.open_workbook(filename)

def q(Str):
    return Str.replace('\ufeff', '')

for i in range(1):
    nrows =  book.sheets()[i+2].nrows
    sheet = book.sheets()[i+2]
    for j in range(2821,2840):
        values_list =  sheet.row_values(j)
        str_values_list = [q(str(k)) for k in values_list]
        #str_values_list[1] = q(str_values_list[1])
        print(str_values_list)
        '''
        for k in values_list:
            print(q(str(k)), str(k))
        '''
        '''
        if(sheet.cell(j,1).ctype != 1):
            values_list[1] = int(values_list[1])
        if(sheet.cell(j,1).ctype != 1):
            print(sheet.cell(j,1).ctype, sheet.cell(j,1).value)
            print(j)
        if(sheet.cell(j,2).value == '黄思琦'):
            print(sheet.cell(j,1).ctype, sheet.cell(j,1).value)
            print('here!!!!')
            break
        
        print(sheet.cell(j,1).ctype, sheet.cell(j,1).value)
        '''