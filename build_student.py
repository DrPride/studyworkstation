# -*- coding: utf-8 -*-
import xlrd
import csv
import os
import database as db

filename = 'data/本研信息.xls'
xlrd.Book.encoding = "utf-8"
book = xlrd.open_workbook(filename)

sql_build = '''create table if not exists student(
        id int primary key not null auto_increment,
        stu_id  varchar(20) ,
        stu_name varchar(16) ,
        stu_type varchar(8),
        stu_sex varchar(2),
        stu_college varchar(32),
        stu_enrollment int,
        stu_class varchar(48)
    )'''

#db.sql_connect_excute(sql_build)
'''
for i in range(5):
#if i == 6: 
    nrows =  book.sheets()[i].nrows
    sheet = book.sheets()[i]
    stu_year = 2018 - i
    for j in range(1,nrows):
        values_list =  book.sheets()[i].row_values(j)
        if(sheet.cell(j,1).ctype != 1):
            values_list[1] = int(values_list[1])
        str_values_list = [str(k).replace('\ufeff', '') for k in values_list]
        if stu_year ==2016:
            str_values_list = str_values_list[:4]+str_values_list[5:6]
        else:
            str_values_list = str_values_list[:5]
        #str_values_list = str_values_list[0:2]+ str_values_list[3:4]+ str_values_list[8:9]+ str_values_list[13:14]
        str_insert = str(str_values_list).strip('[')
        str_insert = str_insert.strip(']')
        #str_insert = "('0'," + str_insert + (',"博士研究生"' if str_values_list[0][1]=='B' else ',"硕士研究生"') +')'
        str_insert = "('0'," + str_insert +',\"' +str(stu_year)+'\"' +',"本科"'+')'

        sql_excute = 'insert ignore into student(id, stu_id, stu_name,stu_sex, stu_college, stu_class,stu_enrollment,stu_type)values'+ str_insert
        #sql_excute = 'insert ignore into student(id, stu_id, stu_name,stu_sex,stu_enrollment, stu_college, stu_type)values'+ str_insert
        print(sql_excute)
        #break
        db.sql_connect_excute(sql_excute)
        '''

i = 6
if i == 6:
    nrows =  book.sheets()[i].nrows
    sheet = book.sheets()[i]
    for j in range(6,nrows):
        values_list =  book.sheets()[i].row_values(j)
        if(sheet.cell(j,1).ctype != 1):
            values_list[1] = int(values_list[1])
        str_values_list = [str(k).replace('\ufeff', '') for k in values_list]
        str_values_list = str_values_list[0:2]+ str_values_list[3:4]+ str_values_list[8:9]+ str_values_list[13:14]
        str_insert = str(str_values_list).strip('[')
        str_insert = str_insert.strip(']')
        str_insert = "('0'," + str_insert + (',"博士研究生"' if str_values_list[0][1]=='B' else ',"硕士研究生"') +')'
        #str_insert = "('0'," + str_insert +',\"' +str(stu_year)+'\"' +',"本科"'+')'

        #sql_excute = 'insert ignore into student(id, stu_id, stu_name,stu_sex, stu_college, stu_class,stu_enrollment,stu_type)values'+ str_insert
        sql_excute = 'insert ignore into student(id, stu_id, stu_name,stu_sex,stu_enrollment, stu_college, stu_type)values'+ str_insert
        print(sql_excute)
        #break
        db.sql_connect_excute(sql_excute)