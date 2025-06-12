from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdminLogin, name='AdminLogin')
]
