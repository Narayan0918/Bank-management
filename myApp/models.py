from django.db import models

# Create your models here.
class BankDetails(models.Model):
    accountNumber = models.BigAutoField(primary_key=True) 
    accountHolder = models.CharField(max_length=40)
    balance = models.FloatField(default=0)
    pin = models.IntegerField(max_length=4)
    bankName = models.CharField(max_length=15)
    mobile = models.BigIntegerField(max_length=10)