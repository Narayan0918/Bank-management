from django.shortcuts import render,redirect
from django.contrib import messages
from myApp.forms import Register,GeneratePin,AmountForm,LoginForm
from myApp.models import BankDetails,Transaction

# Create your views here.

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
    
    return render(request,'register.html',context={'register_form':form})



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


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            acc_num = form.cleaned_data['account_number']
            pin = form.cleaned_data['pin']
            
            try:
                # Check if user exists and PIN matches
                user = BankDetails.objects.get(accountNumber=acc_num)
                if user.pin == pin:
                    # SUCCESS: Store account number in session
                    request.session['account_number'] = user.accountNumber
                    return redirect('dashboard')
                else:
                    messages.error(request, "Incorrect PIN")
            except BankDetails.DoesNotExist:
                messages.error(request, "Account Number does not exist")
    else:
        form = LoginForm()
        
    return render(request, "login.html", {'form': form})

def dashboard_view(request):
    # Check if user is logged in
    if 'account_number' not in request.session:
        return redirect('login')
    
    acc_num = request.session['account_number']
    user = BankDetails.objects.get(accountNumber=acc_num)
    
    # Fetch last 5 transactions (newest first)
    recent_transactions = Transaction.objects.filter(account=user).order_by('-timestamp')[:5]
    
    return render(request, "dashboard.html", {
        'user': user,
        'transactions': recent_transactions
    })

def perform_transaction_view(request, type):
    # type will be either 'deposit' or 'withdraw'
    if 'account_number' not in request.session:
        return redirect('login')
        
    user = BankDetails.objects.get(accountNumber=request.session['account_number'])
    
    if request.method == "POST":
        form = AmountForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            
            if type == 'withdraw':
                if user.balance >= amount:
                    user.balance -= amount
                    Transaction.objects.create(account=user, amount=amount, transaction_type="Debit")
                    messages.success(request, "Withdrawal Successful!")
                else:
                    messages.error(request, "Insufficient Balance")
                    return redirect('dashboard')
            else: # Deposit
                user.balance += amount
                Transaction.objects.create(account=user, amount=amount, transaction_type="Credit")
                messages.success(request, "Deposit Successful!")
            
            user.save()
            return redirect('dashboard')
    else:
        form = AmountForm()
        
    return render(request, "transaction.html", {'form': form, 'type': type})

def logout_view(request):
    try:
        del request.session['account_number']
    except KeyError:
        pass
    return redirect('login')