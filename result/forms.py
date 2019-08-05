from django import forms

from .models import SubjectRegistration

class SubjectRegistrationForm(forms.ModelForm):
    class Meta:
        model = SubjectRegistration
        exclude = ['cls']

        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'pass_mark': forms.NumberInput(attrs={'class': 'form-control'}),
        }
