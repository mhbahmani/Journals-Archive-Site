from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from journals.models import Publication


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label= 'رمز عبور', widget=forms.PasswordInput)


class UploadPublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'pdf',)
        labels = {
            'title': 'عنوان نشریه',
            'pdf': 'فایل نشریه'
        }