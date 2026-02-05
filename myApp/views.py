from django.shortcuts import render
from myApp.forms import Register,Deposit,GeneratePin
from myApp.models import BankDetails

# Create your views here.
def home(request):
    regForm = Register()
    depForm = Deposit()
    genForm = GeneratePin()
    response = render(request,"forms.html",context={'reg':regForm,'dep':depForm,'gen':genForm})
    return response

def register_view(request):
    if request.method == 'POST':
        form = Register(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['fullName']
            mobile_no = form.cleaned_data['mobile']
            initial_balance = form.cleaned_data['balance']
            bank_name = form.cleaned_data['bankName']

            new_account = BankDetails(accountHolder=full_name,mobile=mobile_no,balance=initial_balance,bankName = bank_name)
            new_account.save()

            response = render(request,'success.html',context={'account_number':new_account.accountNumber,'name':new_account.accountHolder})
        else:
            form = Register()
            response = render(request,'register.html',context={'register_form':form})
        return response