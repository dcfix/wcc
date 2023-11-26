from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    quick_checkin = models.CharField(max_length=10, blank=True, null=True,
                                     help_text="A shortcut code for checking in")
    member_since = models.IntegerField(blank=True, null=True)    # keep track of how long someone has been a member
    last_active_date = models.DateField(blank=True, null=True)     # Last time the member paid their membership dues
    birth_date = models.DateField(blank=True, null=True,
                                  help_text="We only track birthday month and year, so day will be set to the 2st. ")

    def __str__(self):
        return self.username
