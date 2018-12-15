# -*- coding:utf-8 -*-
# resources.py
from import_export import resources
from import_export import fields
from data_sql.models import  MainBasicTable, Student

class MainBasicTableResource(resources.ModelResource):
	stu_id = fields.Field(attribute='stu_id', column_name="学号")
	stu_name = fields.Field(attribute='stu_name', column_name="姓名")
	money_count = fields.Field(attribute='money_count', column_name="金额")
	money_year = fields.Field(attribute='money_year', column_name="发放年份")
	money_month = fields.Field(attribute='money_month', column_name="发放月份")
	money_type = fields.Field(attribute='money_type',column_name="资金类型")
	money_organization = fields.Field(attribute='money_organization', column_name="发放组织")
	money_name = fields.Field(attribute='money_name', column_name="资金名称")	


	class Meta:
		model = MainBasicTable
		fields = ['stu_id', 'stu_name',  'money_count', 'money_year', 'money_month', 'money_type', 'money_organization', 'money_name']
		import_id_fields = ['stu_id']
		#fields = ['学号', '姓名',  '金额', '发放年份', '发放月份', '资金类型', '发放组织', '资金名称' ]

class StudentResource(resources.ModelResource):
	class Meta:
		model = Student
		fields = ('学号','姓名','性别','院系','班级')
