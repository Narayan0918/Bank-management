from django import forms

class Register(forms.Form):
    fullName = forms.CharField(label='Full name',max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Enter full name'}))
    mobile = forms.IntegerField(label='Mobile',min_value=6000000000,max_value=9999999999,widget=forms.NumberInput(attrs={'placeholder': 'Enter mobile'}))
    balance = forms.FloatField(label='Initial Balance',min_value=500,widget=forms.NumberInput(attrs={'placeholder': 'Enter minimum amount'}))
    bankName = forms.CharField(label='Bank Name',max_length=15,widget=forms.TextInput(attrs={'placeholder': 'Enter your bank name'}))

class GeneratePin(forms.Form):
    account_number = forms.IntegerField(label='Enter Your Account Number',widget=forms.NumberInput(attrs={'placeholder': 'Enter account number'}))
    pin = forms.IntegerField(label='Set a new 4-Digit PIN',min_value=1000,max_value=9999,widget=forms.NumberInput(attrs={'placeholder': 'Enter PIN'}))

class LoginForm(forms.Form):
    account_number = forms.IntegerField(label='Account Number',widget=forms.NumberInput(attrs={'placeholder': 'Enter account number'}))
    pin = forms.IntegerField(label='Pin',widget=forms.PasswordInput(attrs={'placeholder': 'Enter PIN'}))
    

class AmountForm(forms.Form):
    amount = forms.FloatField(label='Amount',min_value=1,widget=forms.NumberInput(attrs={'placeholder': 'Enter Amount'}))

