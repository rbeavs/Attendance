from django import forms
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'FR', 'SO', 'JR', 'SR', 'event', 'email',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First and Last name'}),
            'FR': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'SO': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'JR': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'SR': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@usd109.org'}),
        }
