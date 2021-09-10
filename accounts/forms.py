from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Publication


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


class UploadPublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'pdf',)