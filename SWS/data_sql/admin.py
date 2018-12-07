from django.contrib import admin

# Register your models here.
from data_sql.models import  Student, MainBasicTable

def make_the_month_9(modeladmin, request, queryset):
	queryset.update(money_month='9')


class MBTAdmin(admin.ModelAdmin): 
	# 需要显示的字段信息 
	list_display = ('id','stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month')
	# 设置哪些字段可以点击进入编辑界面，默认是第一个字段 
	# links 和 editable 不能同时存在
	#list_display_links = ('id', 'stu_id')

	list_editable = ['stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month']

	search_fields = ('stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month')
	
	actions = [make_the_month_9]

admin.site.register(Student)
admin.site.register(MainBasicTable, MBTAdmin)