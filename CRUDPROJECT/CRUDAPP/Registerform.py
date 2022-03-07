import email
from email.headerregistry import Address
from pickle import FALSE
from django import forms
from django.forms.fields import CharField
from spnego import Password

class singup(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(help_text='write your email',)
    Address = forms.CharField(required=FALSE,)
    Technology = forms.CharField(initial='Django',disabled = True,)
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password=forms.CharField(help_text='renter your password',widget=forms.PasswordInput)


