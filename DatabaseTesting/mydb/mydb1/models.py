from django.db import models

# Create your models here.
class Salespeople(models.Model):
    snum = models.IntegerField(primary_key=True)
  
    sname = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    comm = models.DecimalField(max_digits=4, decimal_places=2)