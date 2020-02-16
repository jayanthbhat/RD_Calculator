from django.contrib import admin
from django.urls import path,include
from rd_app.views import home,create_bank_user,BankList,set_rate_of_interest
from .api import BankRateOfInterestValidationAPIView

urlpatterns = [
    path('',home,name="home" ),
    path('bank_list/',BankList,name="BankList"),
    path('create_bank_user/',create_bank_user,name="create_bank_user"),
    path('set_rate_of_interest/<str:pk>',set_rate_of_interest,name="set_rate_of_interest"),
    path('api-get-roi/',BankRateOfInterestValidationAPIView.as_view(),name="api_get-roi")
    
    
  
]