from django.db import models

# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_code = models.CharField(max_length=100, unique=True)
    p_category = models.CharField(max_length=100)
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    p_stockquantity = models.IntegerField()
    p_description = models.TextField()
    p_created_date = models.DateTimeField(auto_now_add=True)
    
class Electronics(Product):
    p_brand = models.CharField(max_length=100)
    p_model = models.CharField(max_length=100)
    p_warranty = models.IntegerField(help_text="Warranty period in months")