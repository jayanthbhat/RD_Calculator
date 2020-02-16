from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .serializers import (BankRateOfInterestAPISerializer)


from rd_app.models import Bank



class BankRateOfInterestValidationAPIView(generics.CreateAPIView):
    serializer_class = BankRateOfInterestAPISerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        bank_name = serializer.data['bank_name']
        print(bank_name)
        deposit_term = serializer.data['deposit_term']
        print(deposit_term)
        bank_details = Bank.objects.filter(bank_name=bank_name)
        if bank_details:   
            if deposit_term == 0:
                content = {
                    "exists":True,
                    "bank_name":bank_details[0].bank_name,
                    "rate_of_interest":bank_details[0].rate_of_interest_1,
                    }
            elif deposit_term == 1:
                content = {
                    "exists":True,
                    "bank_name":bank_details[0].bank_name,
                    "rate_of_interest":bank_details[0].rate_of_interest_2,
                   
                    
                    }
            elif deposit_term == 2:
                content = {
                    "exists":True,
                    "bank_name":bank_details[0].bank_name,
                 
                    "rate_of_interest":bank_details[0].rate_of_interest_3,
                    
                    }
            return Response(content,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)