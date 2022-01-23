from django import forms
from .models import Agent, SocialAccount


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


class SocialAccountForm(forms.ModelForm):
    facebook = forms.URLField(label='Facebook', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    instagram = forms.URLField(label='Instagram', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    linkedin = forms.URLField(label='LinkedIn', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))
    twitter = forms.URLField(label='Twitter', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))

    class Meta:
        model = SocialAccount
        fields = ('facebook', 'instagram', 'linkedin', 'twitter',)
