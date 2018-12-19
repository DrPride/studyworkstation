from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from data_sql import views

urlpatterns = [
    path('restful/', views.MainBasicTableList.as_view()),
    path('graphic_data/', views.MainBasicTableGraphic.as_view()),
    path('graphic_data_year/', views.MainBasicTableGraphicYearList.as_view()),
    path('stu_restful/', views.StudentList.as_view()),
    path('query_params/', views.StudentQueryParamsList.as_view()),
    # path('restful/<>'),
    path('upload/', views.excel_upload),
    #path('test/', views.search)
    # path('<int:pk>', views.PostDetail.as_view()),
]