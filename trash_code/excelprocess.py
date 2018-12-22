# -*- coding: utf-8 -*-
# import file into the mysql
import xlrd
import csv
import os
import database as db
import title_analyze as ta


'''
#print(basic_data_dict[4])
csv_name = 'basic_data_dict.csv'
def csv_writer(csv_name):
    with open(csv_name, "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        for k,v in basic_data_dict[4].items():
            csvWriter.writerow([k,v])
            print(k,v)
        #csvFile.close()
'''

filepath = 'data'
#filename_ass = '月勤工助学工资 - 发银行.xlsx'
'''
file_list = []
for root ,dirs, files in os.walk(filepath):
    file_list = files
    '''
#basic_data_dict = {}

#print(file_list)


for i in file_list:
    #print(i, '\n')
    #flag = i.find('工资')
    if i.find('工资') != -1:
        filename = filepath + '/' + i
    else:
        continue
    
    '''
    book = xlrd.open_workbook(filename)
    table = book.sheets()[0]
    object_name = table.row_values(0)
    object_index = {}
    for j in range(len(object_name)):
        object_index[object_name[j]] = j
    '''
    from content_analyze import file_analyzer as FA
    
    # complete the information of student
    # 班级数据可能不存在
    # if object_index['班级'] == None:
    for m,n,o in zip(table.col_values(object_index['学号']), table.col_values(object_index['姓名']), table.col_values(object_index['班级'])):
        #map[m] = n
        #print(type(m), type(n), m, n, '\n')
        if m == '学号' or n == '姓名':
            continue
        sql = 'insert ignore into student(stu_id, stu_name, stu_class) values (' +'\''+ m +'\'' +','  + "\'"+ n + '\''+','  + "\'"+ o + '\'' + ')'
        try:
            db.sql_connect_excute(sql)
        except Warning as w:
            print(i, '\n')
    #basic_data_dict[i] = map


    # bulid the new table
    # table_name = i[:i.find('工资')]+'工资'
    # table_name 生成逻辑需要重新写
    table_name  = index_map(i)
    # 不仅仅针对 工资表



    # 不设置主键，允许重复记录，因为工资可能多发
    sql_build = '''create table if not exists %s(
        stu_id  varchar(20) ,
        stu_salary int not null,
        money_time varchar(8),
        money_id varchar(20),
        money_reson varchar(20),
        money_pos varchar(20)
    )
    '''%table_name
    print(sql_build)
    # db.sql_connect_excute(sql_build)

'''
    # get the table public information
    info_dict = ta.Titile_Analyze(table_name)
    

    # complete the information of salary_list
    for m,n,o in zip(table.col_values(object_index['学号']), table.col_values(object_index['工资']),table.col_values(object_index['岗位']) ):
        if m == '学号' or n == '姓名':
            continue
        sql = 'insert  into '+ table_name +'(stu_id, stu_salary, money_pos' 
        sql_tail = ') values (' +'\''+ m +'\'' +','  + str(n) + ',' + '\'' + o + '\''
        if info_dict == False:
            sql = sql + sql_tail + ')' 
            #ON DUPLICATE KEY UPDATE stu_salary = stu_salary + VALUES(stu_salary)'
        else:
            sql = sql + ',money_time, money_id, money_reson' + sql_tail + ',\''+ info_dict['time'] + '\''+',\''+ info_dict['id'] + '\'' +',\''+ info_dict['reson'] + '\'' + ')'
            #ON DUPLICATE KEY UPDATE stu_salary = stu_salary + VALUES(stu_salary)'
        print(sql)
        try:
            db.sql_connect_excute(sql)
        except Warning as w:
            print(i, '\n')
    '''
    



