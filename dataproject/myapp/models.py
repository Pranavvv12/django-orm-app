from django.db import models
from django.contrib import admin
# Create your models here.
class Student (models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    referencenumber=models.CharField(max_length=20,help_text="reference number")
    department=models.CharField(max_length=100)
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','email','referencenumber','department')