from django.shortcuts import render,redirect
from django.http import HttpResponse
from Teachers.models import TeacherDatas,NewApplyStudent

def home(request):
    teacherData = TeacherDatas.objects.all()
    return render(request , 'Home.html',{'Teachers':teacherData})

def Apply_student(request):
    Succes=''
    if request.method == "POST":
        name = request.POST.get('name')
        father = request.POST.get('father')
        mother = request.POST.get('Mother')
        number = int(request.POST.get('number'))
        cls = request.POST.get('class')
        image =request.FILES.get('image')
        ApplyStudent = NewApplyStudent.objects.create(
            name =name,
            mother =mother,
            father = father,
            mobile = number,
            cls = cls,
            image = image
        )
        ApplyStudent.save()
        Succes = 'Applyed Succes. Please wite for conformaiton SMS'
        return render(request ,'AppyForm.html', {'Succes':Succes})
    return render(request, 'AppyForm.html')
