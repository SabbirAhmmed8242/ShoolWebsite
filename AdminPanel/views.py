from django.shortcuts import render
from django.contrib.auth import login,authenticate


def AdminLogin(request):
    return render(request, 'AdminLogin.html')
# Create your views here.
