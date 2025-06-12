from django.urls import path
from Students import views
urlpatterns = [
    path('', views.Student, name='Student'),
    path('st-dashbord/', views.st_dashbord, name='st-dashbord'),
    path('st-profile/', views.view_profile, name='view-profile'),

    path('st-login/', views.student_login, name='st-login'),
    path('st-logout/', views.student_logout, name='st-logout'),
    path('st-reg-validity/', views.StudentRegValidityCheck, name='St-Reg-Validity'),
    path('st-reg-form/', views.StudentReg, name='St-Reg'),

    path('ResultFor/', views.ResultFor, name='ResultFor'),
    path('AllStudentResult/', views.AllStudentResult, name='AllStudentResult'),
    path('MarkSheet/', views.IndivisualResult, name='IndvisualResult'),

    path('Upload-data/', views.StudentDetailsData, name='StudentData'),
    path('Dawnload-ID-CARD/', views.IDCARD, name='ID-CARD'),
]
