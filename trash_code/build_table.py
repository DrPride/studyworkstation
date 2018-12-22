# -*- coding: utf-8 -*-
import xlrd
import csv
import os
import database as db


sql_build = '''create table if not exists main_basic_table(
        id int primary key not null auto_increment,
        stu_id  varchar(20) ,
        stu_name varchar(16) ,
        stu_type varchar(4),
        money_count int,
        money_year int,
        money_month varchar(4),
        money_type varchar(8),
        money_organization varchar(16)
    )'''

#db.sql_connect_excute(sql_build)

sql_excute = """
    insert into main_basic_table(money_name) select money_reason from {} 
    where main_basic_table.stu_id = {}.id 
"""

sql_excute2 = """
    update main_basic_table inner join {} on main_basic_table.stu_id={}.stu_id set main_basic_table.money_name={}.money_reason;
"""
'''
table_list = ['nation_reward', 'nation_encouragement', 'nation_support']
for i in table_list:
    db.sql_connect_excute(sql_excute2.format(i,i,i))
'''
