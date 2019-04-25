from django.db import models

class College(models.Model):

    college_name = models.CharField(max_length=250,default='null')
    affliation = models.CharField(max_length=500,default='null')
    college_pic = models.CharField(max_length=1000,default='null')
    college_website=models.CharField(max_length=50,default='null')
    estb = models.CharField(max_length=100,default='null')
    location = models.CharField(max_length=1000,default='null')
    genders = models.CharField(max_length=100,default='null')
    size = models.CharField(max_length=100,default='null')
    faculty = models.CharField(max_length=100,default='null')
    students= models.CharField(max_length=100,default='null')
    fees = models.CharField(max_length=200,default='null')
    pic1=models.CharField(max_length=1000,default='null')
    pic2=models.CharField(max_length=1000,default='null')
    pic3=models.CharField(max_length=1000,default='null')
    pic4=models.CharField(max_length=1000,default='null')
    pic5=models.CharField(max_length=1000,default='null')
    facility1=models.CharField(max_length=1000)
    facility2=models.CharField(max_length=1000)
    facility3=models.CharField(max_length=1000)
    facility4=models.CharField(max_length=1000)
    facility5=models.CharField(max_length=1000)
    course1=models.CharField(max_length=1000)
    course2=models.CharField(max_length=1000)
    course3=models.CharField(max_length=1000)
    course4=models.CharField(max_length=1000)
    course5=models.CharField(max_length=1000)
    course6=models.CharField(max_length=1000)
    course7=models.CharField(max_length=1000)
    contact1=models.CharField(max_length=1000)
    contact2=models.CharField(max_length=1000)
    contact3=models.CharField(max_length=1000)
    def __str__(self):
        return self.college_name 

    