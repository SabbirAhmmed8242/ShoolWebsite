from django.urls import path
from . import views
from .views import AllStudent
urlpatterns = [
    path('', views.teachers, name='Teacher'),
    path('th-login/', views.th_login, name='teacher-login'),
    path('th-registration/', views.th_reg, name='teacher-reg'),
    path('th-logout/', views.th_logout, name='th-logout'),

    path('th-about-form/', views.Teacher_about, name='th-about'),
    path('th-dash/', views.teacherDash, name='th-dashbord'),

    path('add-result/', views.addResult, name='add-result'),
    path('AddResultData/', views.AddResultDataForm, name='AddResultDataForm'),
    path('EditeStudentDataForm/', views.EditeStudentDataForm, name='EditeStudentDataForm'),
    path('AllStudent/', AllStudent.as_view(), name='AllStudentData'),
    # path('AllStudent/', views.AllStudent, name='AllStudentData'),
]