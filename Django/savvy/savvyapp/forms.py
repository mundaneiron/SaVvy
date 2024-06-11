from django import forms
from savvyapp.models import *

class Userinfo(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = "__all__"