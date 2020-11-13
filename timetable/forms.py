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

class SectionSubjectForm(forms.ModelForm):
    class Meta:
        model= SectionSubject
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'additional_teacher': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'no_of_times_a_week': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_before_short_break': forms.CheckboxInput(),
            'is_before_long_break': forms.CheckboxInput(),
        }

class AddTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_periods_a_week': forms.NumberInput(attrs={'class': 'form-control'}),
            'unavailable_days': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class ClassSubjectsForm(forms.ModelForm):
    class Meta:
        model = Class_Subjects
        fields = '__all__'
        widgets = {
            'class_name': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'subjects': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }        

