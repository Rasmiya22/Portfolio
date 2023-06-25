from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    job1=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    degree=models.CharField(max_length=250)
    freelance=models.CharField(max_length=250)
    image1=models.ImageField(upload_to='pics')
    image2 = models.ImageField(upload_to='pics')
    job2=models.CharField(max_length=250)
    company=models.CharField(max_length=250)
    year1=models.CharField(max_length=250)
    jobdesc=models.TextField()

    def __str__(self):
        return self.name

class Qualification(models.Model):
    deg=models.CharField(max_length=250)
    college=models.TextField()
    year=models.TextField()

class Skill(models.Model):
    skill1=models.CharField(max_length=250)
    percentage=models.IntegerField()













