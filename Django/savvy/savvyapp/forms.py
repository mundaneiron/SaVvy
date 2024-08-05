from django import forms
from savvyapp.models import *

class Userinfo(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),  # Use PasswordInput widget for password field
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)