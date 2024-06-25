from django import forms
from savvyapp.models import *

class Userinfo(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = "__all__"

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)