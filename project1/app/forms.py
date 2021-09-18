from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import models
from django.forms import fields


class RegisterUser(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields =['username','email']

  
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email