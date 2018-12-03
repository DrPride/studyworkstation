from django.contrib import admin

# Register your models here.
from data_sql.models import  Student, MainBasicTable


admin.site.register(Student)
admin.site.register(MainBasicTable)
#admin.site.register(NationReward)
