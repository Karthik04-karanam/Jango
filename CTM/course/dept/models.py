from django.db import models

# Create your models here.
class Department(models.Model):
    c_name = models.CharField(max_length=100)
    c_duration = models.IntegerField()
    c_fees = models.DecimalField(max_digits=10, decimal_places=2)
    trainer_name = models.CharField(max_length=100)
    mode=models.CharField(max_length=50, choices=[('online', 'Online'), ('offline', 'Offline')])
    no_of_seats = models.IntegerField()
