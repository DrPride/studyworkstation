from django.contrib import admin
from django.db.models import F
# Register your models here.
from data_sql.models import  Student, MainBasicTable
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from data_sql.resources import MainBasicTableResource, StudentResource

def make_the_month_9(modeladmin, request, queryset):
	queryset.update(money_month='9')

def MakeTheIntTimeTen(modeladmin, request, queryset):
	queryset.update(money_count = F('money_count')*10)

def MakeTheIntDivideTen(modeladmin, request, queryset):
	queryset.update(money_count = F('money_count')/10)


class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource

class MBTImport_Export(ImportExportActionModelAdmin, ImportExportModelAdmin):
	resource_class = MainBasicTableResource


class MBTAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin): 
	# 需要显示的字段信息 
	list_display = ('id','stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month')

	list_editable = ['stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month']

	search_fields = ('stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month')
	
	actions = [MakeTheIntTimeTen, MakeTheIntDivideTen]

	resource_class = MainBasicTableResource

admin.site.register(Student, StudentAdmin)
admin.site.register(MainBasicTable, MBTAdmin)