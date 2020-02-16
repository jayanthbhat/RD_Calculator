from rest_framework import serializers

import datetime
import uuid

from rd_app.models import Bank
from django.utils import timezone


class BankRateOfInterestAPISerializer(serializers.Serializer):
    bank_name = serializers.CharField()
    deposit_term = serializers.IntegerField()
