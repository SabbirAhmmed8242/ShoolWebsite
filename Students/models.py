from django.db import models

class Student_login_details(models.Model):
    name=models.CharField(max_length=50)
    studentID = models.IntegerField()
    password = models.CharField(max_length=120)
    def __str__(self):
        return str(self.studentID)
    
class StudentRegInfoAdmin(models.Model):
    StudentID = models.IntegerField()
    ProvidedStNumber = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.StudentID)
    
class StudentRegLogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=120)
    ST_NUMBER = models.CharField(max_length=15)
    cls = models.CharField(max_length=10)
    image = models.ImageField(upload_to='students/')
    StudentID = models.IntegerField()


    def __str__(self):
        return str(self.StudentID)
    

class StudentDetails(models.Model):
    name = models.CharField(max_length=30)
    father = models.CharField(max_length=30)
    mother = models.CharField(max_length=30)
    studentID = models.IntegerField()
    mobile = models.IntegerField()
    email = models.EmailField(max_length=25)
    cls = models.CharField(max_length=8)
    image = models.ImageField(upload_to='StudenDetailsImage')

    def __str__(self):
        return str(self.studentID)
# Create your models here.
