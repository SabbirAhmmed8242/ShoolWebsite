from django.db import models

class ClassSixResults(models.Model):
    name = models.CharField(max_length=30)
    studentID = models.IntegerField()
    year = models.IntegerField()
    bangla = models.IntegerField()
    english = models.IntegerField()
    math = models.IntegerField()
    biology = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()
    avarage = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.studentID)
    
class ClassSevenResults(models.Model):
    name = models.CharField(max_length=30)
    studentID = models.IntegerField()
    year = models.IntegerField()
    bangla = models.IntegerField()
    english = models.IntegerField()
    math = models.IntegerField()
    biology = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()
    avarage = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.studentID)
    
class ClassEightResults(models.Model):
    name = models.CharField(max_length=30)
    studentID = models.IntegerField()
    year = models.IntegerField()
    bangla = models.IntegerField()
    english = models.IntegerField()
    math = models.IntegerField()
    biology = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()
    avarage = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.studentID)
    

class ClassNineResults(models.Model):
    name = models.CharField(max_length=30)
    studentID = models.IntegerField()
    year = models.IntegerField()
    bangla = models.IntegerField()
    english = models.IntegerField()
    math = models.IntegerField()
    biology = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()
    avarage = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.studentID)

class ClassTenResults(models.Model):
    name = models.CharField(max_length=30)
    studentID = models.IntegerField()
    year = models.IntegerField()
    bangla = models.IntegerField()
    english = models.IntegerField()
    math = models.IntegerField()
    biology = models.IntegerField()
    chemistry = models.IntegerField()
    physics = models.IntegerField()
    avarage = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return str(self.studentID)
# Create your models here.
