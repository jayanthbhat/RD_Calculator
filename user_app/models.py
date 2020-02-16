from django.db import models
# Importing AbstractUser to extend
from django.contrib.auth.models import AbstractUser 
import uuid
from rd_app.models import Bank


# Extending Abstract User
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Bank'),

    )
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES,
        default=1,
    )
    bank = models.ForeignKey(Bank, related_name='UserBank', on_delete=models.SET_NULL, blank=True, null=True)