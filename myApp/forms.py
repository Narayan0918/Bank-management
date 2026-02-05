from django import forms

class Register(forms.Form):
    fullName = forms.CharField(label='Full name',max_length=40)
    mobile = forms.IntegerField(label='Mobile',min_value=6000000000,max_value=9999999999)
    balance = forms.FloatField(label='Initial Balance',min_value=500)
    bankName = forms.CharField(label='Bank Name',max_length=15)


class GeneratePin(forms.Form):
    pin = forms.IntegerField(label='Create Pin')

class Deposit(forms.Form):
    amount = forms.FloatField(label='Deposite Amount')

class Withdraw(forms.Form):
    amount = forms.FloatField(label='Withdraw Amount')

