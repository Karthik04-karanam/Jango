from django.db import models

# Create your models here.
class Details(models.Model):
    e_name = models.CharField(max_length=100)
    e_id = models.CharField(max_length=50, unique=True)
    e_email = models.EmailField()
    e_department = models.CharField(max_length=100)
    e_job_role = models.CharField(max_length=100)
    e_salary = models.DecimalField(max_digits=10, decimal_places=2)
    e_date_of_joining = models.DateField()

    
