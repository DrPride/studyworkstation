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

class StudentFieldSerializer(serializers.ModelSerializer):
    # stu_id = serializers.CharField(label='stu_id', read_only=True)
    # stu_sex = serializers.CharField(label='stu_sex', read_only=True)
    stu_enrollment = serializers.IntegerField(label='stu_enrollment', read_only=True)
    stu_college = serializers.CharField(label='stu_enrollment', read_only=True)
    # stu_type = serializers.CharField(label='stu_type', read_only=True)
    stu_class = serializers.CharField(label='stu_class', read_only=True)

    class Meta:
        model = Student
        fields = ['stu_enrollment', 'stu_college', 'stu_class']


class MainBasicTableSerializer(serializers.ModelSerializer):
    stu_id = serializers.CharField(source='stu_id.stu_id')
    stu_sex = serializers.CharField(source='stu_id.stu_sex')
    stu_enrollment = serializers.IntegerField(source='stu_id.stu_enrollment')
    stu_college = serializers.CharField(source='stu_id.stu_college')
    stu_type = serializers.CharField(source='stu_id.stu_type')

    
    class Meta:
        model = MainBasicTable
        fields = '__all__'
        #fields = ['stu_id', 'stu_sex','stu_enrollment', 'stu_college', 'stu_type']

class MainBasicTableGraphicSerializer(serializers.ModelSerializer):
    stu_type = serializers.CharField(label='stu_type', read_only=True)
    count = serializers.IntegerField(label='count', read_only=True)

    class Meta:
        model = MainBasicTable
        fields = ['stu_type','money_type','money_name', 'count']

class MainBasicTableGraphicYearSerializer(serializers.ModelSerializer):
    money_year = serializers.IntegerField(label='money_year', read_only=True)

    class Meta:
        model = MainBasicTable
        fields = ['money_year']
        #fields = ['money_year', 'money_count', 'stu_college', 'stu_enrollment', 'stu_class']
