from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    stream = models.CharField(max_length=2)
    student_id = models.CharField(max_length=5)
    is_present = models.BooleanField(default=True)
    date = models.DateField()
  