from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("patient_name", "date_birth", "email", "phone", "gender", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()
