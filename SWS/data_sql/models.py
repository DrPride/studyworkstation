# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainBasicTable(models.Model):
    stu_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='学号')
    stu_name = models.CharField(max_length=16, blank=True, null=True, verbose_name='姓名')
    stu_type = models.CharField(max_length=8, blank=True, null=True, verbose_name='学生类型')
    stu_sex = models.CharField(max_length=2, blank=True, null=True, verbose_name='性别')
    stu_college = models.CharField(max_length=32, blank=True, null=True, verbose_name='院系')
    stu_enrollment = models.IntegerField(blank=True, null=True, verbose_name='入学年份')
    stu_class = models.CharField(max_length=48, blank=True, null=True, verbose_name='班级')
    money_count = models.IntegerField(blank=True, null=True, verbose_name='金额')
    money_year = models.IntegerField(blank=True, null=True, verbose_name='发放年份')
    money_month = models.CharField(max_length=4, blank=True, null=True, verbose_name='发放月份')
    money_type = models.CharField(max_length=8, blank=True, null=True, verbose_name='资金类型')
    money_organization = models.CharField(max_length=16, blank=True, null=True, verbose_name='发放组织')
    money_name = models.CharField(max_length=64, blank=True, null=True, verbose_name='资金名称')

    class Meta:
        managed = True
        verbose_name_plural = '资金发放表单'
        db_table = 'main_basic_table'


class NationEncouragement(models.Model):
    stu_id = models.CharField(max_length=20, blank=True, null=True)
    stu_name = models.CharField(max_length=16, blank=True, null=True)
    stu_class = models.CharField(max_length=20, blank=True, null=True)
    stu_account = models.CharField(max_length=20, blank=True, null=True)
    money_count = models.IntegerField(blank=True, null=True)
    money_reason = models.CharField(max_length=20, blank=True, null=True)
    money_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nation_encouragement'


class NationReward(models.Model):
    stu_id = models.CharField(max_length=20, blank=True, null=True)
    stu_name = models.CharField(max_length=8, blank=True, null=True)
    stu_class = models.CharField(max_length=20, blank=True, null=True)
    stu_account = models.CharField(max_length=20, blank=True, null=True)
    money_count = models.IntegerField(blank=True, null=True)
    money_reason = models.CharField(max_length=20, blank=True, null=True)
    money_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nation_reward'


class NationSupport(models.Model):
    stu_id = models.CharField(max_length=20, blank=True, null=True)
    stu_name = models.CharField(max_length=16, blank=True, null=True)
    stu_class = models.CharField(max_length=20, blank=True, null=True)
    stu_account = models.CharField(max_length=20, blank=True, null=True)
    money_count = models.IntegerField(blank=True, null=True)
    money_reason = models.CharField(max_length=20, blank=True, null=True)
    money_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nation_support'


class Student(models.Model):
    stu_id = models.CharField(max_length=20, blank=True, null=True, verbose_name='学号')
    stu_name = models.CharField(max_length=16, blank=True, null=True, verbose_name='姓名')
    stu_type = models.CharField(max_length=8, blank=True, null=True, verbose_name='学生类型')
    stu_sex = models.CharField(max_length=2, blank=True, null=True, verbose_name='性别')
    stu_college = models.CharField(max_length=32, blank=True, null=True, verbose_name='院系')
    stu_enrollment = models.IntegerField(blank=True, null=True, verbose_name='入学年份')
    stu_class = models.CharField(max_length=48, blank=True, null=True, verbose_name='班级')

    class Meta:
        managed = True
        verbose_name_plural = '学生信息表'
        db_table = 'student'
