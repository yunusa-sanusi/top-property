from django import forms
from .models import Agent


class AgentForm(forms.ModelForm):
    address = forms.CharField(label='Address', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    profile_picture = forms.FileField(label='Profile Picture', widget=forms.FileInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    bio = forms.CharField(label='Bio', widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg form-control-a'}))

    class Meta:
        model = Agent
        fields = ('address', 'age', 'phone_number', 'profile_picture', 'bio',)
