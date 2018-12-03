from django.shortcuts import render
from rest_framework import generics

# Import into database
import xlrd
from django.db import transaction
#from drf_multiple_model.views import ObjectMultipleModelAPIView

# restful_api
from data_sql.models import MainBasicTable,Student
from data_sql.serializers import MainBasicTableSerializer


from django.http import HttpResponse
import os
import pymysql

# Create your views here.



def index(request):
    return render(request,"index.html", locals())



def excel_upload(request):
    if request.method == "POST":
        upload_file = request.FILES['myfile']
        type_excel = upload_file.name.split('.')[1]
        if type_excel == 'xlsx':
            # 得到后缀名后开始解析
            wb = xlrd.open_workbook(filename=None, file_contents = upload_file.read())
            table = wb.sheets()[0]
            nrows = table.nrows
            try:
                with transaction.atomic():
                    for i in range(1, nrows):
                        rowValues = table.row_values(i)
                        #print(rowValues)
                        for j in range(len(rowValues)):
                            # 学号格式转换
                            if(table.cell(i,j).ctype == 2):
                                rowValues[j] = int(rowValues[j])
                        # 解决\ufeff转码问题
                        str_values_list = [str(k).replace('\ufeff', '') for k in rowValues]
                        #print(str_values_list)
                        # stu_type 根据 stu_id 生成
                        object_name_list = ['stu_id', 'stu_name',  'money_count', 'money_year', 
                        'money_month', 'money_type', 'money_organization', 'money_name']
                        create_dict = dict(zip(object_name_list,str_values_list))
                        
                        
                        #add_list = ['stu_sex','stu_college','stu_enrollment','stu_type']
                        querySet = Student.objects.get(stu_id=create_dict['stu_id'])
                        create_dict['stu_sex'] = querySet.stu_sex
                        create_dict['stu_college'] = querySet.stu_college
                        create_dict['stu_enrollment'] = querySet.stu_enrollment
                        create_dict['stu_type'] = querySet.stu_type

                        #print(create_dict)
                        MainBasicTable.objects.create(**create_dict)  
            except Exception as e:
                print(e)
                return HttpResponse('Error on Data')

            return HttpResponse('OK')
        
        return HttpResponse('文件后缀应该是应该是xlsx')

    return HttpResponse('Not POST')


'''
class SixmonthList(generics.ListCreateAPIView):
	queryset =Sixmonth.objects.all()
    # 上边这个是查询集，可以通过这个直接进行查询
	serializer_class = sixmonthSerializer

class NationRewardList(generics.ListCreateAPIView):
    queryset = NationReward.objects.all()
    serializer_class = NationRewardSerializer
'''


class MainBasicTableList(generics.ListCreateAPIView):
    serializer_class = MainBasicTableSerializer


    def get_queryset(self):
        queryset = MainBasicTable.objects.all()
        #filter_fields = ('stu_id', 'stu_name', 'stu_type', 'monet_count', 'money_year', 'money_month', 'money_type', 'money_organization')
        query_list = ['stu_id', 'stu_name', 'stu_sex','stu_college',
        'stu_enrollment','stu_type', 'monet_count', 'money_year', 
        'money_month', 'money_type', 'money_organization']
         
        query_res = self.request.GET.dict()
        query_key = list(query_res.keys())
        #print(query_key)
        for i in query_key:
            query_res[i+'__contains'] = query_res.pop(i)
        
        print(query_key,query_res)
        if query_res is not None:
            queryset = queryset.filter(**query_res)
        #str_query = query_res['stu_name']
        #queryset = queryset.filter(stu_name__icontains='易')
        # 事实证明queryset的模糊查询是支持的，说明是传入参数的方式不对
        #queryset = queryset.filter(stu_name__icontains ='易')
        #print(str_query)
        #print(query_res['stu_name__icontains'])
        return queryset
        
        


    




