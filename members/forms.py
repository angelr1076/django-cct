from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class ProfilePageForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic')

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfilePageForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].label = "Profile Avatar"
        

