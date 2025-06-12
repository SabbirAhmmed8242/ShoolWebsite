from django.shortcuts import render,redirect
from . models import Student_login_details,StudentDetails,StudentRegLogin,StudentRegInfoAdmin
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password,make_password
from Results.models import ClassEightResults,ClassSevenResults,ClassNineResults,ClassSixResults,ClassTenResults
from django.views.generic import ListView,CreateView
import pandas as pd


def Student(request):
    if 'student_id' in request.session:
        return redirect('st-dashbord')
    if 'teacher_login' in request.session:
        return redirect('th-dashbord')
    return render(request, 'Student.html')

def student_login(request):
    if 'teacher_login' in request.session:
        return redirect('th-dashbord')
    if "student_id" in request.session:
        return redirect('st-dashbord')
    if request.method == 'POST':
        username = request.POST.get('name')
        studentID = request.POST.get('StudentID')
        password = request.POST.get('password')
        request.session['studenID'] = studentID
        try:
            Student = Student_login_details.objects.get(studentID = studentID)
            if check_password(password, Student.password):
                request.session['student_id'] = Student.id
                
                try:
                    StudentDetails.objects.get(studentID = studentID)
                    return redirect('st-dashbord')
                except StudentDetails.DoesNotExist:
                    return redirect('StudentData')
            else:
                print('err')
                return render(request, 'Home.html' )
        except Student_login_details.DoesNotExist:
            return render(request, 'StudentLogin.html', {'error': 'Invalid ID'})
    return render(request, 'StudentLogin.html')

def view_profile(request):
    return render(request, 'Profile.html')

def StudentRegValidityCheck(request):
    if 'teacher_login' in request.session:
        return redirect('th-dashbord')
    if "student_id" in request.session:
        return redirect('st-dashbord')
    if request.method == 'POST':
        StudentID = request.POST.get('StudentID')
        ST_NUMBER = request.POST.get('ST_NUMBER')
        request.session["ST_NUMBER"] = ST_NUMBER
        request.session['StudentID'] = StudentID
        try:
            D_ST_NUMBER = StudentRegInfoAdmin.objects.get(StudentID=StudentID)
        except:
            return HttpResponse('Student ID missmatch')
        if ST_NUMBER == D_ST_NUMBER.ProvidedStNumber:
            return redirect('St-Reg')
    return render(request, 'StudentRegValidty.html')

def StudentReg(request):
    if 'teacher_login' in request.session:
        return redirect('th-dashbord')
    if "student_id" in request.session:
        return redirect('st-dashbord')
    ST_NUMBER = request.session.get('ST_NUMBER')
    StudentID = request.session.get('StudentID')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')
        cls = request.POST.get('cls')
        image = request.FILES.get('image')
        request.session['image']= image
        if password == con_password:
            m_password = make_password(password)
            NewStudent=StudentRegLogin.objects.create(
                username = username,
                password = m_password,
                ST_NUMBER = ST_NUMBER,
                cls = cls,
                image = image,
                StudentID = StudentID
            )
            NewStudent.save()
            LoginDetails = Student_login_details.objects.create(
                name = username,
                studentID = StudentID,
                password = m_password
            )
            LoginDetails.save()
            return redirect('st-login')
    return render(request, 'StudentRegForm.html',{'ST_NUMBER':ST_NUMBER , 'StudentID':StudentID})

def StudentDetailsData(request):
    if 'student_id' not in request.session:
        return redirect('st-login')
    StudentID = request.session.get('StudentID')
    StudentID = request.session.get('studenID')
    print(StudentID)
    St = StudentRegLogin.objects.filter(StudentID = StudentID).first()
    image = St.image if St else None
    if request.method == "POST":
        name = request.POST.get('name')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        mobile = request.POST.get('mobile')
        email = request.POST.get('mail')
        cls = request.POST.get('cls')
        ck = StudentDetails.objects.filter(studentID=StudentID).first()
        if not ck:
            DataSave = StudentDetails.objects.create(
                name = name,
                father = father,
                mother = mother,
                mobile = mobile,
                email = email,
                cls = cls,
                image = image,
                studentID = StudentID
            )
            DataSave.save()
            return redirect('st-dashbord')
        
        else:
            return render(request, "StudentDetails.html", {'error': 'Student ID already exists', 'StdentID': StudentID})
    return render(request, "StudentDetails.html", {'StdentID': StudentID})

def IDCARD(request):
    if 'teacher_login' in request.session:
        return redirect('th-dashbord')
    StudentID = request.session.get('StudentID')
    StudentID = request.session.get('studenID')
    profile = StudentDetails.objects.get(studentID = StudentID)
    return render(request, 'IDCard.html',{'ID':StudentID,'profile':profile})

def ResultFor(request):
    studentID = request.session.get('studenID')
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        if form_type == 'all_result':
            cls_All = request.POST.get('class')
            year_all = request.POST.get('year')
            request.session['cls_all'] = cls_All
            request.session['year_all'] = year_all
            return redirect('AllStudentResult')
        elif form_type == 'ind_result':
            cls_ind = request.POST.get('ind_class')
            year_ind = request.POST.get('passing_year')
            request.session['cls_ind'] = cls_ind
            request.session['year_ind'] = year_ind
            request.session['studentid'] = studentID
            return redirect('IndvisualResult')
    return render(request,'ResultFor.html',{'studentID':studentID})

def IndivisualResult(request):
   
    if "student_id" not in request.session:
        return redirect('st-login')
    cls_ind = request.session.get('cls_ind')
    year_ind = request.session.get('year_ind')
    studentId = request.session.get('studenID')
    if cls_ind == 'Six':
        result = ClassSixResults.objects.filter(studentID = studentId, year=year_ind)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Seven':
        result = ClassSevenResults.objects.filter(studentID = studentId, year=year_ind)
        print(result)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Eight':
        result = ClassEightResults.objects.filter(studentID = studentId, year=year_ind)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Nine':
        result = ClassNineResults.objects.filter(studentID = studentId, year=year_ind)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Ten':
        result = ClassTenResults.objects.filter(studentID = studentId, year=year_ind)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    
    return render(request,"IndivisualResultOrMarkSheet.html")

def AllStudentResult(request):
    cls_all = request.session.get('cls_all')
    year_all = request.session.get('year_all')
    print(cls_all , year_all)
    results = None

    if cls_all == 'Six':
        results = ClassSixResults.objects.filter(year=year_all)
        print(results)
        return render(request , 'AllStudentResult.html' ,{'result':results , 'Class':cls_all, 'year': year_all})
    elif cls_all == 'Seven':
        results = ClassSevenResults.objects.filter(year=year_all)
        return render(request , 'AllStudentResult.html' ,{'result':results , 'Class':cls_all, 'year': year_all})
    elif cls_all == 'Eight':
        results = ClassEightResults.objects.filter(year=year_all)
        return render(request , 'AllStudentResult.html' ,{'result':results , 'Class':cls_all, 'year': year_all})
    elif cls_all == 'Nine':
        results = ClassNineResults.objects.filter(year=year_all)
        return render(request , 'AllStudentResult.html' ,{'result':results , 'Class':cls_all, 'year': year_all})
    elif cls_all == 'Ten':
        results = ClassTenResults.objects.filter(year=year_all)
        return render(request , 'AllStudentResult.html' ,{'result':results , 'Class':cls_all, 'year': year_all})
    return render(request, 'AllStudentResult.html')

def student_logout(request):
    request.session.flush()
    return redirect('st-login')
    # try:
    #     del request.session['student_id']
    #     return redirect('st-login')
    # except TypeError:
    #     pass
    # return render(request , 'LtudentLogin.html')

def st_dashbord(request):
    if 'student_id' not in request.session:
        return redirect('st-login')
    if 'teacher_login' in request.session:
        return redirect('th-dashbord')
    StudentID = request.session.get('studenID')
    profile = StudentDetails.objects.filter(studentID = StudentID).first()
    return render(request, 'Dashbord.html',{'profile':profile})

# Create your views here.
