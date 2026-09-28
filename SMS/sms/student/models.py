from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=100)
    s_enrollment_number = models.CharField(max_length=20, unique=True)
    s_email = models.EmailField(unique=True)
    s_phone_number = models.IntegerField()
    s_course = models.CharField(max_length=100)
    s_year=models.IntegerField()
    s_date_of_admission = models.DateField()

    
