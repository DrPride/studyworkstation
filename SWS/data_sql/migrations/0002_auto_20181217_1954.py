# Generated by Django 2.1.3 on 2018-12-17 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_sql', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainbasictable',
            name='stu_class',
        ),
        migrations.RemoveField(
            model_name='mainbasictable',
            name='stu_college',
        ),
        migrations.RemoveField(
            model_name='mainbasictable',
            name='stu_enrollment',
        ),
        migrations.RemoveField(
            model_name='mainbasictable',
            name='stu_sex',
        ),
        migrations.RemoveField(
            model_name='mainbasictable',
            name='stu_type',
        ),
    ]
