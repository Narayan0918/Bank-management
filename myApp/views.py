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
            return response
    else:
        form = Register()
        response = render(request,'register.html',context={'register_form':form})
    return response



def set_pin_view(request):
    message = ''
    if request.method=='POST':
        form = GeneratePin(request.POST)

        if form.is_valid():
            acc_num = form.cleaned_data['account_number']
            new_pin = form.cleaned_data['pin']

            try:
                user_account = BankDetails.objects.get(accountNumber =  acc_num)

                if user_account.pin is not None:
                    message = 'PIN already exist for this account!'
                else:
                    user_account.pin = new_pin
                    user_account.save()
                    message = 'Success! Your pin has been set.'
            except BankDetails.DoesNotExist:
                message = 'Account Number not found.'
    else:
        form = GeneratePin()
    response = render(request,'set_pin.html',context={'form':form,'message':message}) 
    return response