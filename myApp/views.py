from django.shortcuts import render
from myApp.forms import Register,Deposit,GeneratePin
# Create your views here.
def home(request):
    regForm = Register()
    depForm = Deposit()
    genForm = GeneratePin()
    response = render(request,"forms.html",context={'reg':regForm,'dep':depForm,'gen':genForm})
    return response