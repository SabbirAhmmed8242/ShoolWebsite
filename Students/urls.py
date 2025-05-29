from django.urls import path
from Students import views
urlpatterns = [
    path('', views.Student, name='Student'),
    path('st-login/', views.student_login, name='st-login'),
    path('st-logout/', views.student_logout, name='st-logout'),
    path('st-dashbord/', views.st_dashbord, name='st-dashbord'),
    path('ResultFor/', views.ResultFor, name='ResultFor'),
    path('AllStudentResult/', views.AllStudentResult, name='AllStudentResult'),
    path('MarkSheet/', views.IndivisualResult, name='IndvisualResult'),
    path('Upload-data/', views.StudentDetailsData, name='StudentData')
]
