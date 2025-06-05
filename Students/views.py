from django.shortcuts import render,redirect
from . models import Student_login_details
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from Results.models import ClassEightResults,ClassSevenResults,ClassNineResults,ClassSixResults,ClassTenResults
from Students.models import StudentDetails
from django.views.generic import ListView,CreateView
def Student(request):
    return render(request, 'Student.html')


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        studentID = request.POST.get('StudentID')
        password = request.POST.get('password')
        request.session['studenID'] = studentID
        try:
            Student = Student_login_details.objects.get(studentID = studentID)
            if password == Student.password:
                request.session['student_id'] = Student.id 
                return redirect('st-dashbord')
            else:
                print('err')
                return render(request, 'Home.html' )
        except Student_login_details.DoesNotExist:
            return render(request, 'StudentLogin.html', {'error': 'Invalid ID'})
    return render(request, 'StudentLogin.html')

def StudentDetailsData(request):
    if 'student_id' not in request.session:
        return redirect('st-login')
    if request.method == "POST":
        name = request.POST.get('name')
        father = request.POST.get('father')
        mother = request.POST.get('mother')
        mobile = request.POST.get('mobile')
        email = request.POST.get('mail')
        cls = request.POST.get('cls')
        image = request.FILES.get('image')
        studentID = request.session.get('studentID')
        ck = StudentDetails.objects.filter(studentID=studentID).first()
        if not ck:
            DataSave = StudentDetails.objects.create(
                name = name,
                father = father,
                mother = mother,
                mobile = mobile,
                email = email,
                cls = cls,
                image = image,
                studentID = studentID
            )
            DataSave.save()
            return render(request, "StudentDetails.html",{'Succes':'Data Upload Succes'})
        else:
            return HttpResponse('Student ID already exist')
    return render(request, "StudentDetails.html")

def ResultFor(request):
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
            studentID = request.POST.get('studentID')
            request.session['cls_ind'] = cls_ind
            request.session['year_ind'] = year_ind
            request.session['studentid'] = studentID
            return redirect('IndvisualResult')
    return render(request,'ResultFor.html')

def IndivisualResult(request):
    if "student_id" not in request.session:
        return redirect('st-login')
    cls_ind = request.session.get('cls_ind')
    year_ind = request.session.get('year_ind')
    studentId = request.session.get('studentid')

    if cls_ind == 'Six':
        result = ClassSixResults.objects.filter(studentID = studentId)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Seven':
        result = ClassSevenResults.objects.filter(studentID = studentId)
        print(result)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Eight':
        result = ClassEightResults.objects.filter(studentID = studentId)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Nine':
        result = ClassNineResults.objects.filter(studentID = studentId)
        return render(request , 'IndivisualResultOrMarkSheet.html',{'result':result,'year':year_ind})
    elif cls_ind == 'Ten':
        result = ClassTenResults.objects.filter(studentID = studentId)
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
    try:
        del request.session['student_id']
        return redirect('st-login')
    except TypeError:
        pass
    return render(request , 'LtudentLogin.html')

def st_dashbord(request):
    if 'student_id' not in request.session:
        return request('st-login')
    return render(request, 'Dashbord.html')

# Create your views here.
