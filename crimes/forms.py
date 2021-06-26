from django.forms import ModelForm
from django import forms
from crimes.models import Crime

class NewCrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ('suspect', 'crime_type', 'address', 'city', 'state', 'photo_main', 'description',)
        
        widgets = {
            'suspect': forms.Select(attrs={'class': 'form-control'}),
            'crime_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
        
class UpdateCrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ('suspect', 'crime_type', 'address', 'city', 'state', 'solved', 'photo_main', 'description',)
        
        widgets = {
            'suspect': forms.Select(attrs={'class': 'form-control'}),
            'crime_type': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'crime_date': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }