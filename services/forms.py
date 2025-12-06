from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-3', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
