from django.db import models
import random
from django.utils import timezone

def generate_account_number():
    while True:
        acc_num = random.randint(999210000000,999999999999)
        if not BankDetails.objects.filter(accountNumber = acc_num).exists():
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
    

class Transaction(models.Model):
    # Link this transaction to a specific Bank Account
    account = models.ForeignKey(BankDetails, on_delete=models.CASCADE, related_name='transactions')
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=10)  # "Deposit" or "Withdraw"
    timestamp = models.DateTimeField(auto_now_add=True) # Automatically sets current date/time

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.timestamp}"