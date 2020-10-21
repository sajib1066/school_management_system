from django import forms
from .models import *
from flatpickr import TimePickerInput

class PeriodForm(forms.ModelForm):
    class Meta:
        model = Period
        fields = '__all__'
        widgets = {
            'section': forms.Select(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': TimePickerInput(attrs={'class': 'form-control'}),
            'end_time': TimePickerInput(attrs={'class': 'form-control'})
        }

class BreakForm(forms.ModelForm):
    class Meta:
        model = Breaks
        fields = '__all__'
        widgets = {
            'break_type': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'start_time': TimePickerInput(attrs={'class': 'form-control'}),
            'end_time': TimePickerInput(attrs={'class': 'form-control'})
        }  

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        widgets = {
            'school_class': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'period': forms.Select(attrs={'class': 'form-control'}),
        }              

