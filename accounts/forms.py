from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class': 'sign_up_in-user-inputs',
                                                                                      'placeholder': 'Username'}))
    password = forms.CharField(label="", max_length=20, widget=forms.PasswordInput(attrs={'class': 'sign_up_in-user-inputs',
                                                                                          'placeholder': 'Password'}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class': 'sign_up_in-user-inputs',
                                                                                      'placeholder': 'Username'}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'sign_up_in-user-inputs',
                                                                      'placeholder': 'Email'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'sign_up_in-user-inputs',
                                                                            'placeholder': 'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'sign_up_in-user-inputs',
                                                                            'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email']
