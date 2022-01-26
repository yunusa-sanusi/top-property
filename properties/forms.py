from django import forms
from .models import Amenity, Property, PropertyImage


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('address', 'city', 'country', 'zipcode', 'beds', 'baths',
                  'garage', 'area', 'description', 'price', 'property_picture', 'video', 'property_type', 'status',)
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'beds': forms.NumberInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'baths': forms.NumberInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'garage': forms.NumberInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'area': forms.NumberInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'price': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'property_picture': forms.FileInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'video': forms.FileInput(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'property_type': forms.Select(attrs={'class': 'form-control form-control-lg form-control-a'}),
            'status': forms.Select(attrs={'class': 'form-control form-control-lg form-control-a'})
        }


class AmenityForm(forms.ModelForm):
    amenity = forms.CharField(max_length=500, label='Amenities (Seperated by commas)', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg form-control-a'}))

    class Meta:
        model = Amenity
        fields = ('amenity',)


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ('image',)
        labels = {
            'image': 'Images'
        }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg form-control-a', 'multiple': True})
        }
