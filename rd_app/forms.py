from django import forms

from django.forms import Form, ModelForm, FileField

from .models import RecuringDeposit,Bank
class RDForm(forms.ModelForm):
    
    amount = forms.IntegerField(label=("Enter Amount to be Deposited *"),required=False)
    rate_of_interest = forms.CharField(label=("RATE OF INTEREST"),required=False)
    class Meta:
        model = RecuringDeposit
        fields = ['bank_name','amount','deposit_term','rate_of_interest']
        labels  = {
        'bank_name': 'Select Bank ',
        'deposit_term': 'Select Deposit Term',
    
        }

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['rate_of_interest_1','rate_of_interest_2','rate_of_interest_3']