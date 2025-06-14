from django.db import models

class teacher_login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=120)
    m_number = models.IntegerField()
    NID = models.IntegerField()

    def __str__(self):
        return self.username
    
class TeacherDatas(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.IntegerField()
    Join_date = models.DateField()
    add = models.CharField(max_length=55)
    sub = models.CharField(max_length=20)
    image = models.ImageField(upload_to='TeachersImage/')
    ST_COODE = models.CharField(max_length=18)
    NID = models.IntegerField(null=True)
    def __str__(self):
        return self.name

    
class secret_number_and_NID(models.Model):
    st_number = models.CharField(max_length=18)
    NID = models.IntegerField()
    
    def __str__(self):
        return self.st_number
    
class NewApplyStudent(models.Model):
    name = models.CharField(max_length=30)
    mother = models.CharField(max_length=30)
    father = models.CharField(max_length=30)
    mobile = models.IntegerField()
    cls = models.CharField(max_length=10)
    image = models.ImageField(upload_to='NewStudentApplys/')

    def __str__(self):
        return self.name
# Create your models here.
