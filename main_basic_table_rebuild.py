# -*- coding: utf-8 -*-
import xlrd
import csv
import os
import database as db

filename = 'data/2018年国家奖助学金发放表10.29.xlsx'
xlrd.Book.encoding = "utf-8"
book = xlrd.open_workbook(filename)

sql_build = '''create table if not exists main_basic_table(
        id int primary key not null auto_increment,
        stu_id  varchar(20),
        stu_name varchar(16),
        stu_type varchar(8),
        stu_sex varchar(2),
        stu_college varchar(32),
        stu_enrollment int,
        stu_class varchar(48),
        money_count int,
        money_year int,
        money_month varchar(4),
        money_type varchar(8),
        money_organization varchar(16),
        money_name varchar(64)
    )'''

db.sql_connect_excute(sql_build)
for i in range(3):
    # print(i)
    #object_name = book.sheets()[i].row_values(0)
    #print(object_name)
    nrows =  book.sheets()[i].nrows
    if i == 2:
        nrows += 1
    sheet = book.sheets()[i]
    for j in range(1,nrows-1):
        values_list =  book.sheets()[i].row_values(j)
        if(sheet.cell(j,1).ctype != 1):
            values_list[1] = int(values_list[1])
        str_values_list = [str(k).replace('\ufeff', '') for k in values_list]
        str_values_list = str_values_list[1:3]+ str_values_list[5:7]
        str_insert = str(str_values_list).strip('[')
        str_insert = str_insert.strip(']')
        str_insert = "('0',"  + str_insert + ',"本科","奖助学金","2018")'
        sql_excute = 'insert ignore into main_basic_table(id,stu_id,stu_name,money_count,money_name,stu_type,money_type, money_year)'+' values' +str_insert
        print(sql_excute)
        db.sql_connect_excute(sql_excute)
    print(i)

        


