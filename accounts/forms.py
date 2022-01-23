from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-control-a'}))
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg form-control-a'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'username', 'password1', 'password2')


class UpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'username',)
