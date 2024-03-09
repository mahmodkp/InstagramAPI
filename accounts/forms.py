from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    This form is used for creating a new user
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'mobile', )


class CustomUserChangeForm(UserChangeForm):
    """
    This form is used for changing current user
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'mobile',)

# # accounts/forms.py
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ("username", "email")
