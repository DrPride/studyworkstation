# -*- coding: utf-8 -*-
import pymysql
import warnings as warns


def sql_connect_excute(sql):
	conn = pymysql.connect(host='127.0.0.1', 
		port=3306, 
		user='root', 
		passwd='118270',
		db='studyworkstation')

	cur = conn.cursor()
	try:
		cur.execute(sql)
		conn.commit()
		#print('执行成功')
	except Exception as e:
		raise e
	finally:
		cur.close()
	conn.close()
	
	