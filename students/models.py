from django.db import models

# Create your models here.
class Student(models.Model):
    f_name=models.CharField(max_length=100)
    l_name=models.CharField(max_length=100)
    birth_date=models.DateField()
