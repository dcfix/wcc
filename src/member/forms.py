from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "quick_checkin", "first_name", "last_name",
                  "birth_date", "last_active_date", "member_since")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "quick_checkin", "first_name", "last_name",
                  "birth_date", "last_active_date", "member_since")
