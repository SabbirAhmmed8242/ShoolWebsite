from django.db import models

class Student_login_details(models.Model):
    name=models.CharField(max_length=50)
    studentID = models.IntegerField()
    password = models.CharField(max_length=120)
    def __str__(self):
        return str(self.studentID)
    
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
