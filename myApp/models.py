from django.db import models
import random

def generate_account_number():
    while True:
        acc_num = random.randint(999210000000,999999999999)
        if not BankDetails.objects.filter(accountNumber = acc_num).exist():
            return acc_num


# Create your models here.
class BankDetails(models.Model):
    accountNumber = models.BigAutoField(primary_key=True,default=generate_account_number,editable=False) 
    accountHolder = models.CharField(max_length=40)
    balance = models.FloatField(default=0)
    pin = models.IntegerField(null=True,blank=True)
    bankName = models.CharField(max_length=15)
    mobile = models.BigIntegerField()

    def __str__(self):
        return f"{self.accountNumber} - {self.accountHolder}"