from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from user_app.models import User
from rd_app.models import RecuringDeposit,Bank 
from .forms import *
from babel.numbers import format_currency,format_number

def formated_currency(value):
    ind_currency = format_currency(value, 'INR', locale='en_IN')
    currency = ind_currency[:ind_currency.index('.')]
    return currency

def formated_number(value):
    number_format = format_number(value, locale='en_IN')
    return number_format

def claculate_rd_amount(amount_recvd,term,roi):

    if term == 0:
        term = 12
    elif term == 1:
        term = 24
    elif term == 2:
        term = 48
    term_derived = term+1
    cals= ((amount_recvd) * (term) * (term_derived) * (roi))
    total= int(cals/2400)
    return total

def home(request):
    active=False
    bank_details=Bank.objects.all()
    rd_status = RecuringDeposit.objects.all()
    form = RDForm()
    if request.method == "POST":
        form = RDForm(request.POST)
        if form.is_valid():
            active=True
            form.save()
            bank_name=form.cleaned_data.get('bank_name')
            
            amount_recvd=form.cleaned_data.get('amount')
            term=form.cleaned_data.get('deposit_term')
            roi=form.cleaned_data.get('rate_of_interest')
            interest_amount=claculate_rd_amount(int(amount_recvd),int(term),float(roi))
            if term == 0:
                term = 12
            elif term == 1:
                term = 24
            elif term == 2:
                term = 48

            if bank_name == 0:
                bank_name='BANK 1'
            elif bank_name == 1:
                bank_name='BANK 2'
            elif bank_name == 2:
                bank_name='BANK 3'
            total_amount= amount_recvd*term  
            maturity=interest_amount+total_amount


            return render(request,'home.html',context={
                'amount':amount_recvd,
                'bank_name':bank_name,
                'deposit_term':term,
                'rate_of_interest':roi,
                'maturity':formated_currency(maturity),
                'interest_amount':interest_amount,
                'interest_amount_currency':formated_currency(interest_amount),
                'total_amount':total_amount,
                'total_amount_currency':formated_currency(total_amount),
                'amount_rs':formated_currency(amount_recvd)
                })
        return redirect('/')

    return render(request,'home.html',context={'form':form,'bank_details':bank_details,'active':active})

def BankList(request):
    ban_data=Bank.objects.all()
    return render(request,'bank_home.html',context={'ban_data':ban_data,}) 

def set_rate_of_interest(request,pk=None):
    bank=get_object_or_404(Bank,pk=pk)
    print(bank)
    form = BankForm(instance=bank)
    print(form)
    if request.method == "POST":
        form = BankForm(request.POST,instance=bank)
        print(form)
        if form.is_valid():
            print("validated")
            roi=request.POST.get('rate_of_interest_1', False)
            
            print(roi)
            form.save()
        else:
            print("not validated")

           
        return redirect('/bank_list/')
    return render(request,'set_bank_rate_of_interest.html',context={'bank':bank,'form':form})

def create_bank_user(request):
    user_name1 = User.objects.create_user(username='bank_1',password='bank_1',user_type=2)
    user_name1.save()
    user_name2 = User.objects.create_user(username='bank_2',password='bank_2',user_type=2)
    user_name2.save()
    user_name3 = User.objects.create_user(username='bank_3',password='bank_3',user_type=2)
    user_name3.save()
    return HttpResponse("Bank users created")