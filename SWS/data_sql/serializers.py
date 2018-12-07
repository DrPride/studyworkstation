from rest_framework import serializers
from data_sql.models import  MainBasicTable, Student#Sixmonth, NationReward, 

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
    
    class Meta:
        model = MainBasicTable
        fields = '__all__'



