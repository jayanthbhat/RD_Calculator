from django.contrib import admin

# Register your models here.
from .models import RecuringDeposit,Bank

admin.site.register(RecuringDeposit)
admin.site.register(Bank)
