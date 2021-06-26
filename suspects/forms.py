from django.forms import ModelForm
from django import forms
from .models import Suspect


class NewSuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        fields = ('first_name', 'last_name', 'mugshot', 'description', 'in_custody')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'in_custody': forms.CheckboxInput(attrs={'class': 'form-check-input ml-3'}),
        }


class SuspectEditForm(forms.ModelForm):
    class Meta:
        model = Suspect
        fields = ('first_name', 'last_name', 'mugshot', 'description', 'in_custody')
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'in_custody': forms.CheckboxInput(attrs={'class': 'form-check-input ml-3'}),
        }