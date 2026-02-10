from django import forms

class Register(forms.Form):
    fullName = forms.CharField(label='Full name',max_length=40)
    mobile = forms.IntegerField(label='Mobile',min_value=6000000000,max_value=9999999999)
    balance = forms.FloatField(label='Initial Balance',min_value=500)
    bankName = forms.CharField(label='Bank Name',max_length=15)

class GeneratePin(forms.Form):
    account_number = forms.IntegerField(label='Enter Your New Account Number')
    pin = forms.IntegerField(label='Set a new 4-Digit PIN',min_value=1000,max_value=9999)

class Login(forms.Form):
    account_number = forms.IntegerField(label='Account Number')
    pin = forms.IntegerField(label='Pin',widget=forms.PasswordInput)
    

class AmountForm(forms.Form):
    amount = forms.FloatField(label='Amount',min_value=1)

