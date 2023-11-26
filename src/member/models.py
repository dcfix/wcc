from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    quick_checkin = models.CharField(max_length=10,
                                     help_text="A shortcut code for checking in")
    member_since = models.IntegerField()    # keep track of how long someone has been a member
    last_active_date = models.DateField()     # Last time the member paid their membership dues
    birthday = models.DateField(help_text="We only track birthday month and year, so day will be set to the 1st. ")

    def __str__(self):
        return self.username
