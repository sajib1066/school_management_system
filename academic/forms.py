from django import forms
from . import models
from academic.models import ClassRegistration


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = models.ClassInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = models.Section
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 2018/2019 session'}),
        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = models.Session
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }

class ShiftForm(forms.ModelForm):
    class Meta:
        model = models.Shift
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClassRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClassRegistration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'class_name': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'class_session': forms.Select(attrs={'class': 'form-control'}),
            'shift': forms.Select(attrs={'class': 'form-control'}),
            'guide_teacher': forms.Select(attrs={'class': 'form-control'}),
        }

class GuideTeacherForm(forms.ModelForm):
    class Meta:
        model = models.GuideTeacher
        fields = '__all__'
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }

class ChangeSessionForm(forms.ModelForm):
    class Meta:
        model=models.currentsession
        fields = '__all__'
        widgets = {
            'current': forms.Select(attrs={'class': 'form-control'}),
        }
