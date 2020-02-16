from django.db import models
# from user_app.models import User
# Create your models here.
class RecuringDeposit(models.Model):
    BANK_CHOICES = (
        (0, 'BANK 1'),
        (1, 'BANK 2'),
        (2, 'BANK 3'), # Pending is Rejected
    )
    bank_name = models.PositiveSmallIntegerField(
        choices=BANK_CHOICES,
        default=0,
    )

    amount = models.IntegerField(null=True,blank=True)
    DEPOSIT_TERM_CHOICES = (
        (0, '12'),
        (1, '24'),
        (2, '48'), # Pending is Rejected
    )
    deposit_term = models.PositiveSmallIntegerField(
        choices=DEPOSIT_TERM_CHOICES,
        default=0,
    )
    rate_of_interest = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.bank_name

class Bank(models.Model):
    BANK_CHOICES = (
        (0, 'BANK 1'),
        (1, 'BANK 2'),
        (2, 'BANK 3'), # Pending is Rejected
    )
    bank_name = models.PositiveSmallIntegerField(
        choices=BANK_CHOICES,
        default=0,
    )
    DEPOSIT_TERM_CHOICES = (
        (0, '12'),
        (1, '24'),
        (2, '48'), # Pending is Rejected
    )
    deposit_term = models.PositiveSmallIntegerField(
        choices=DEPOSIT_TERM_CHOICES,
        default=0,
    )
    rate_of_interest_1 = models.FloatField(null=True,blank=True)
    rate_of_interest_2 = models.FloatField(null=True,blank=True)
    rate_of_interest_3 = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.bank_name)

# class SetRateOfInterest(models.Model):
#     user= models.ForeignKey(User, related_name='CreatedByUser', on_delete=models.SET_NULL, blank=True, null=True) # set null till dev
#     rd_map=models.ForeignKey(RecuringDeposit,related_name='rd_mapping', on_delete=models.SET_NULL, blank=True, null=True)
#     rate_of_interest = models.FloatField(null=True,blank=True)

