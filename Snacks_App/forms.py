from django import forms
from Snacks_App.models import *
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# this registerform is for the form on my register.html page
class RegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Your Username*', widget= forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Enter your username'}
    ))

    email = forms.EmailField(widget= forms.EmailInput(
        attrs = {'class':'form-control', 'placeholder':'Enter your email*'}
    ))

    first_name = forms.CharField(label = 'Your Firstname',required = False, widget= forms.TextInput(
        attrs= {'class':'form-control', 'placeholder':'Enter your firstname'}
    ))

    last_name = forms.CharField(label = 'Your Lastname', required = False, widget= forms.TextInput(
        attrs= {'class':'form-control', 'placeholder':'Enter your lastname'}
    ))

    password1 = forms.CharField(label = 'Your Password*', widget= forms.PasswordInput(
        attrs={'class':'form-control', 'placeholder':'Enter your password'}
    ))

    password2 = forms.CharField(label = 'Confirm Password*', widget= forms.PasswordInput(
        attrs= {'class':'form-control', 'placeholder':'Confirm your password'}
    ))

    botcather = forms.CharField(required = False, widget= forms.HiddenInput(), validators=[validators.MaxLengthValidator(1), ]
    )

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        # fields = '__all__'
        # exclude = ['date_joined', 'firstname']......it will inherit everything on the models user and exclude this

# this is to save your data.
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name= self.cleaned_data['last_name']
        if commit:
            user.save()
            return user

# this is to check that 2 people doesn't sign up with this email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ooops! sorry, Email already exists')
        return email

# class PlaceOrderForm(forms.ModelForm):
#     Username
#     Email
#     Choice_of_snacks
#     Date_needed
#     Order Description
#     Delivery method
    


