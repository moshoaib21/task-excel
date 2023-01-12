from django.db import models

# Create your models here.
class Department(models.Model):
    dep_num=models.IntegerField()
    dep_name=models.CharField(max_length=200)

class Employee(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    gender=models.CharField(max_length=20)
    address=models.TextField(max_length=200)
    salary=models.IntegerField()

class xl(models.Model):
    file=models.FileField(upload_to="excel")