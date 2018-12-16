from django.contrib import admin
from django.db.models import F
# Register your models here.
from data_sql.models import  Student, MainBasicTable
from data_sql.resources import MainBasicTableResource, StudentResource

from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


def make_the_month_9(modeladmin, request, queryset):
	queryset.update(money_month='9')

def MakeTheIntTimeTen(modeladmin, request, queryset):
	queryset.update(money_count = F('money_count')*10)

def MakeTheIntDivideTen(modeladmin, request, queryset):
	queryset.update(money_count = F('money_count')/10)

def CompleteTheData(modeladmin, request, queryset):
	queryset_pluge = Student.objects.all()
	for i in queryset:
		try:
			add_item = queryset_pluge.get(stu_id=i.stu_id)
			name_list = ['stu_type', 'stu_sex','stu_college','stu_enrollment']
			for j in name_list:
				i.__dict__[j] = add_item.__dict__[j]
			i.save()
		except Exception as e:
			pass
		
CompleteTheData.short_description = '填充学生基本信息'


class StudentAdmin(ImportExportModelAdmin):
	list_display = ['stu_id', 'stu_name', 'stu_type', 'stu_sex','stu_college','stu_enrollment']

	#form = TheStudentDownloadButton

	list_display_links = ['stu_id']
	search_fields = ('stu_id', 'stu_enrollment')
	resource_class = StudentResource




class MBTAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin): 
	# 需要显示的字段信息 
	list_display = ('stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month')

	list_display_links = ['stu_id']

	list_editable = [ 'stu_name','money_name','money_count', 'money_year', 'money_month']

	search_fields = ('stu_id', 'stu_name','money_name','money_count', 'money_year', 'money_month')
	
	actions = [CompleteTheData]


	resource_class = MainBasicTableResource

admin.site.register(Student, StudentAdmin)
admin.site.register(MainBasicTable, MBTAdmin)