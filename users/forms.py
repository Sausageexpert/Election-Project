from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Students
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs={'class':'special'}), label = '')
    identity = forms.CharField(widget = forms.TextInput(attrs={'class':'special'}), label = '')
    class Meta():
        model=Students
        fields=['name','identity']