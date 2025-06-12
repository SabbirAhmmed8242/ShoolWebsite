from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . models import teacher_login,secret_number_and_NID,TeacherDatas
from Results.models import ClassSixResults,ClassSevenResults,ClassEightResults,ClassTenResults,ClassNineResults
from Students.models import StudentDetails
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
def teachers(request):
    if 'student_id' in request.session:
        return redirect('st-dashbord')
    if 'teacher_login' in request.session:
        return redirect('th-dashbord')
    return render(request, 'Teachers.html')

def th_login(request):
    if 'student_id' in request.session:
        return redirect('st-dashbord')
    if request.method == "POST":
        username   = request.POST.get("username").strip()
        password   = request.POST.get("password").strip()
        nb_number  = request.POST.get("nbNumber").strip()
        request.session['username'] = username
        try:
            Teacher = teacher_login.objects.filter(username = username).first()
        except teacher_login.DoesNotExist:
            return HttpResponse('username invalid')


        if password != Teacher.password:
            return HttpResponse('Password not match')

        if nb_number != str(Teacher.m_number).strip():
            print(nb_number)
            print(Teacher.m_number)
            return HttpResponse('Mobile number missmatch')
        request.session["teacher_login"] = Teacher.id
        return redirect('th-dashbord')
    return render(request, 'TeacherLogin.html')

@never_cache
def addResult(request):
    if 'teacher_login' not in request.session:
        return redirect('teacher-login')
    if request.method == "POST":
        cls = request.POST.get('class')
        year = request.POST.get('year')
        request.session['Selected_class'] = cls
        request.session['Selected_year'] = year
        if cls in ["Class: Six", "Class: Seven", "Class: Eight", "Class: Nine", "Class: Ten"]:
            return redirect('AddResultDataForm')           
    return render(request, 'AddResultForm.html')

def AddResultDataForm(request):
    if 'teacher_login' not in request.session:
        return redirect('teacher-login')

    cls = request.session.get('Selected_class')
    year = request.session.get('Selected_year')
    if request.method == "POST":
        name =  request.POST.get('name')
        studentID = request.POST.get('studentID')
        Bangla =  int(request.POST.get('Bangla'))
        English =  int(request.POST.get('English'))
        Biology =  int(request.POST.get('Biology'))
        Chemistry =  int(request.POST.get('Chemistry'))
        Physics =  int(request.POST.get('Physics'))
        Math = int(request.POST.get('Math'))
        total = (Bangla + English + Biology + Math + Chemistry + Physics)
        avarage = total/6
        if cls == 'Class: Six':
            Six = ClassSixResults.objects.create(
                name = name,
                studentID = studentID,
                year = year,
                bangla = Bangla,
                english = English,
                math =Math,
                biology = Biology,
                chemistry = Chemistry,
                physics = Physics,
                avarage = avarage,
                total = total
            )
            Six.save()
            succes = 'Result Add Succesfully'
            return render(request, 'AddResultDataForm.html', {'succes': succes})
        elif cls == 'Class: Seven':
            Seven = ClassSevenResults.objects.create(
                name = name,
                studentID = studentID,
                year = year,
                bangla = Bangla,
                english = English,
                math =Math,
                biology = Biology,
                chemistry = Chemistry,
                physics = Physics,
                avarage = avarage,
                total = total
            )
            Seven.save()
        elif cls == 'Class: Eight':
            Eight = ClassEightResults.objects.create(
                name = name,
                studentID = studentID,
                year = year,
                bangla = Bangla,
                english = English,
                math =Math,
                biology = Biology,
                chemistry = Chemistry,
                physics = Physics,
                avarage = avarage,
                total = total
            )
            Eight.save()
        elif cls == 'Class: Nine':
            Nine = ClassNineResults.objects.create(
                name = name,
                studentID = studentID,
                year = year,
                bangla = Bangla,
                english = English,
                math =Math,
                biology = Biology,
                chemistry = Chemistry,
                physics = Physics,
                avarage = avarage,
                total = total
            )
            Nine.save()
        elif cls == 'Class: Ten':
            Ten = ClassTenResults.objects.create(
                name = name,
                studentID = studentID,
                year = year,
                bangla = Bangla,
                english = English,
                math =Math,
                biology = Biology,
                chemistry = Chemistry,
                physics = Physics,
                avarage = avarage,
                total = total
            )
            Ten.save()
            
    return render(request, 'AddResultDataForm.html')

def th_logout(request):
    request.session.flush()
    return redirect('teacher-login')
    # try:
    #     del request.session['teacher_login']
    #     return redirect('teacher-login')
    # except TypeError:
    #     pass

def th_reg(request):
    if request.method == "POST":
        username = request.POST.get('username')
        NID = request.POST.get('NID')
        MoNumber = request.POST.get('MoNumber')
        ST_number = request.POST.get('secret_number')
        password = request.POST.get('password')

        request.session['ST_NUMBER'] = ST_number
        try:
            secret = secret_number_and_NID.objects.get(NID = NID , st_number = ST_number)
            reg = teacher_login.objects.create(
                username =username , 
                NID= NID , 
                m_number = MoNumber ,
                password = password)
            reg.save()
            return redirect('th-about')
        except:
            err = 'NID or Secrite code not match'
            return render(request,'TeacherReg.html', {'err':err} )
    return render(request , 'TeacherReg.html')

def Teacher_about(request):

    ST_NUMBER = request.session.get('ST_NUMBER')

    if request.method == "POST":
        name = request.POST.get('name')
        M_number = request.POST.get('M_number')
        join_date = request.POST.get('Join_date')
        sub = request.POST.get('sub')
        address = request.POST.get('addr')
        image = request.FILES.get('image')

        infoAdd = TeacherDatas.objects.create(
            name = name,
            mobile = M_number,
            Join_date = join_date,
            add = address,
            sub = sub,
            image =image,
            ST_COODE = ST_NUMBER
        )
        infoAdd.save()
        return redirect('teacher-login')
    return render(request, 'TeacherAboutForm.html', {'ST_NUMBER':ST_NUMBER})

@never_cache
def EditeStudentDataForm(request):
    if 'teacher_login' not in request.session:
        return redirect('teacher-login')
    if request.method == "POST":
        cls = request.POST.get('selected_class')
        request.session['selected_class'] = cls
        return redirect('AllStudentData')
    return render(request, 'EditeStudentDataForm.html')

# THIS IS A ALL STUDENT LIST
# - using class
class AllStudent(ListView):
    model = StudentDetails
    context_object_name = 'students'
    template_name='AllStudent.html'

    def get_queryset(self):
        cls = self.request.session.get('selected_class')
        if cls:
            return StudentDetails.objects.filter(cls = cls)
        return StudentDetails.objects.none()

# - using view

# def AllStudent(request):
#     cls = request.session.get('selected_class')
#     if cls:
#         Data = StudentDetails.objects.filter(cls = cls)
#         return render(request, 'AllStudent.html' , {'Data':Data})
#     return render(request, 'AllStudent.html')

@never_cache
def teacherDash(request):
    if 'teacher_login' not in request.session:
        return redirect('teacher-login')
    username = request.session.get('username')
    print(username)
    Teacherinfo = TeacherDatas.objects.filter(name = username).first()
    teacherdata = TeacherDatas.objects.all()
    print(teacherdata)
    return render(request, 'Teacherdashbord.html',{'Teacherinfo':Teacherinfo, 'teacherData': teacherdata})



# def UpdateInfo(request , pk):
#     info = get_object_or_404(TeacherDatas, pk = pk)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         mobile = request.POST.get('number')
        
#         info.name = name
#         info.mobile = mobile
#         info.save()
#         return redirect('th-dashbord')
#     return render(request, 'TeacherDetailUpdateForm.html',{'info':info})

def DeleteInfo(request):
    if request.method == 'POST':
        ST_CODE = request.POST.get('ST-CODE')
        DATABASE_ST_CODE = secret_number_and_NID.objects.filter(st_number = ST_CODE)

        if DATABASE_ST_CODE.exists():
            TeacherAboutInfo = TeacherDatas.objects.filter(ST_COODE = ST_CODE)
            TeacherAboutInfo.delete()
            return redirect('th-about')
        else:
            return HttpResponse('ST-CODE not match')
    return render(request , 'TeacherDetailUpdateForm.html')