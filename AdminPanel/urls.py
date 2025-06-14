from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from AdminPanel import views
urlpatterns = [
    path('',views.AdminLogin, name='AdminLogin'),



    path('dashboard/', views.AdminDashboard, name='admin-dashboard'),
    path('SelectResultsFor/', views.Results, name='SelectResultsFor'),
    path('AdminTeacher/', views.TeachersAdmin, name='TeacherAdmin'),
    path('AdminStudents/',views.AdminStudent , name='AdminStudents'),

    
    path('DeleteTeachers/',views.DeleteTeacher , name='DelTeachers'),
    path('ADD-TEACHER/',views.ADD_TEACHER , name='add-teacher'),
    path('update-teacher', views.UpdateTeacherInfoAdmin, name='update-teachers'),
    path('ADD_NID_ST/', views.ADD_ST_NID_NUM, name='ADD-ST-NID'),
    path('delete-nid-st/', views.DeleteStNid, name='DELETE-NID-ST'),
]
