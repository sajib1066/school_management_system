from django import forms

from .models import AcademicInfo

class AcademicInfoForm(forms.ModelForm):
    class Meta:
        model = AcademicInfo
        exclude = ['class_info']
        widgets = {
            'class_info': forms.Select(attrs={'class': 'forms-control'}),
            'roll': forms.TextInput(attrs={'class': 'form-control'})
        }
