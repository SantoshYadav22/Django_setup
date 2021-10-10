from django.db import models

# Create your models here.

class Student(models.Model):
    studid=models.IntegerField()
    studname=models.CharField(max_length=100)
    studmail=models.EmailField(max_length=70)
    studpass=models.CharField(max_length=100)
    comment=models.CharField(max_length=100, default='not available')
