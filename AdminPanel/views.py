from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from Teachers.models import *
from Students.models import *

def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        # Check user exists
        if not User.objects.filter(username=username).exists():
            return render(request, 'AdminLogin.html', {'err': 'Invalid username'})

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin-dashboard') 
        else:
            return render(request, 'AdminLogin.html', {'err': 'Invalid credentials or not an admin'})

    return render(request, 'AdminLogin.html')

# Only superuser access
@login_required(login_url='AdminLogin')
@user_passes_test(lambda u: u.is_superuser)
def AdminDashboard(request):
    teachers = TeacherDatas.objects.all()
    student = Student_login_details.objects.all()
    return render(request, 'Admindashbord.html',{'teachers':teachers,'students':student})

@login_required
def Results(request):
    return render(request, 'Results.html')

@login_required(login_url='AdminLogin')
def AdminStudent(request):
    return render(request, 'AminStudents.html')

@login_required
def TeachersAdmin(request):
    ST_NUMBER_NID = TeacherDatas.objects.all()
    
       
    return render(request, 'AdminTeachers.html',{'ST_NUMBER':ST_NUMBER_NID})

def DeleteTeacher(request):
    if request.method =='POST':
        number = request.POST.get('number')
        NID = request.POST.get('NID')
        TH_ST_NID_DATA = secret_number_and_NID.objects.filter(NID=NID)
        TH_LOGIN_DATA = teacher_login.objects.filter(m_number = number)
        TH_DATA = TeacherDatas.objects.filter(mobile=number)

        if TH_DATA.exists() and TH_LOGIN_DATA.exists() and TH_ST_NID_DATA.exists():
            TH_ST_NID_DATA.delete()
            TH_LOGIN_DATA.delete()
            TH_DATA.delete()
            return redirect('TeacherAdmin')
        else:
            return render(request, 'AdminTeachers.html', {'err':'INVALID'})
        
def ADD_TEACHER(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('mobile')
        subject = request.POST.get('subject')
        image = request.FILES.get('image')
        ST_NUMBER = request.POST.get('st_number')
        NID = request.POST.get('nid')
        address = request.POST.get('address')
        join_date = request.POST.get('join_date')
        password = request.POST.get('password')
        m_pass = make_password(password)
        TH_LOGIN = teacher_login.objects.all()
        if (teacher_login.objects.filter(m_number = number).exists() and 
            TeacherDatas.objects.filter(mobile = number).exists() and 
            secret_number_and_NID.objects.filter(NID = NID).exists()):
           
           return HttpResponse('NID or mobile number exists')

        teacher_login.objects.create(
            username = name,
            password = m_pass,
            NID = NID,
            m_number = number
        )

        TeacherDatas.objects.create(
            name = name,
            mobile = number,
            Join_date = join_date,
            add= address,
            sub = subject,
            ST_COODE = ST_NUMBER,
            image = image,
            NID = NID,
        )

        secret_number_and_NID.objects.create(
            st_number = ST_NUMBER,
            NID = NID
        )
        return redirect('TeacherAdmin')
    return render(request, 'ADD_TEACHER.html')

def UpdateTeacherInfoAdmin(request):
    NID= request.session.get('NID')
    number = request.session.get('number')
    print(number)
    print(NID)
    teacher = TeacherDatas.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        subject = request.POST.get('subject')
        ST_NUMBER = request.POST.get('st_number')
        NID= request.POST.get('NID')
        join_date = request.POST.get('joiin_date')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        try: 
            TH_LOLGIN_OBJ = teacher_login.objects.get(m_number = mobile)
            TH_LOLGIN_OBJ.username =name
            TH_LOLGIN_OBJ.m_number = mobile
            TH_LOLGIN_OBJ.NID = NID
            TH_LOLGIN_OBJ.save()

            TH_DATA_OBJ = TeacherDatas.objects.get(mobile = mobile)
            TH_DATA_OBJ.name = name
            TH_DATA_OBJ.mobile = mobile
            TH_DATA_OBJ.add = address
            TH_DATA_OBJ.sub = subject
            TH_DATA_OBJ.Join_date = join_date
            TH_DATA_OBJ.image = image 
            TH_DATA_OBJ.ST_COODE = ST_NUMBER
            TH_DATA_OBJ.NID = NID
            TH_DATA_OBJ.save()

            TH_ST_NID_OBJ = secret_number_and_NID.objects.get(NID = NID)
            TH_ST_NID_OBJ.st_number = ST_NUMBER
            TH_ST_NID_OBJ.NID = NID
            TH_ST_NID_OBJ.save()
            return redirect('TeacherAdmin')
        except:
            return render(request, 'TeacherUpdateAdmin.html',{'err':'Invalid'})
    return render(request, 'TeacherUpdateAdmin.html',{'teacher':teacher})

def ADD_ST_NID_NUM(request):
    st_number = secret_number_and_NID.objects.all()
    if request.method == "POST":
        ST_CODE = request.POST.get('st_code')
        NID = request.POST.get('nid-up')
        if secret_number_and_NID.objects.filter(st_number= ST_CODE, NID = NID ).exists():
            return render(request, 'ADDST_CODE_AND_NID_TEACHER.html',{'err':'Already exists','st_nid':st_number})
        else:
            secret_number_and_NID.objects.create(
                st_number = ST_CODE,
                NID = NID
            )
            return render(request, 'ADDST_CODE_AND_NID_TEACHER.html',{'success':'Add Succesfully','st_nid':st_number})
    return render(request, 'ADDST_CODE_AND_NID_TEACHER.html',{'st_nid':st_number})

def DeleteStNid(request):
    st_number = secret_number_and_NID.objects.all()
    if request.method == 'POST':
        ST_CODE = request.POST.get('ST_CODEE')
        NID = request.POST.get('NIDS')
        Avality=secret_number_and_NID.objects.filter(st_number = ST_CODE, NID =NID)
        if Avality.exists():
            Avality.delete()
            return redirect('ADD-ST-NID')
        else:
            return redirect('admin-dashboard')
    return render(request, 'ADDST_CODE_AND_NID_TEACHER.html',{'st_nid':st_number})