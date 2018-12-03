import database as db
sql = """insert into student(stu_id, stu_name) values('101', '102')"""
db.sql_connect_excute(sql)