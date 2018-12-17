from rest_framework import serializers
from data_sql.models import  MainBasicTable, Student #Sixmonth, NationReward, 

'''
class sixmonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sixmonth
        fields = '__all__'
        #read_only_fields = '__all__'

class NationRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationReward
        fields = '__all__'
'''

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['stu_id','stu_sex','stu_enrollment', 'stu_college', 'stu_type']



class MainBasicTableSerializer(serializers.ModelSerializer):
    stu_id = serializers.CharField(source='stu_id.stu_id')
    stu_sex = serializers.CharField(source='stu_id.stu_sex')
    stu_enrollment = serializers.CharField(source='stu_id.stu_enrollment')
    stu_college = serializers.CharField(source='stu_id.stu_college')
    stu_type = serializers.CharField(source='stu_id.stu_type')

    
    class Meta:
        model = MainBasicTable
        fields = '__all__'
        #fields = ['stu_id', 'stu_sex','stu_enrollment', 'stu_college', 'stu_type']

class MainBasicTableGraphicSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(label='count', read_only=True)

    class Meta:
        model = MainBasicTable
        fields = ['stu_type','money_type','money_name', 'count']

