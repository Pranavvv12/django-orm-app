# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:

### STEP 2:

### STEP 3:

Write your own steps

## PROGRAM
```python
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
```

## OUTPUT

## RESULT
Thus the project is developed to have Student information database.
