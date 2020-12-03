from django import forms
from . import models
from academic.models import ClassRegistration
from flatpickr import DatePickerInput

session_choices = (
        ('2018/2019', '2018/2019'),
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022'),
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026'),
    )
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
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
            'start_date': DatePickerInput(attrs={'class': 'form-control'}),
            'end_date': DatePickerInput(attrs={'class': 'form-control'}),
            'name': forms.Select(attrs={'class': 'form-control'}),
            'term': forms.Select(attrs={'class': 'form-control'}),
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
            'class_name': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.Select(attrs={'class': 'form-control'}),
            'guide_teacher': forms.Select(attrs={'class': 'form-control'}),
        }


class ChangeSessionForm(forms.ModelForm):
    class Meta:
        model=models.currentsession
        fields = '__all__'
        widgets = {
            'current': forms.Select(attrs={'class': 'form-control'}),
        }

class SelectClassForm(forms.Form):
    class_select = (
        (1, 'Playgroup'),
        (2, 'Pre-nursery'),
        (3, 'Nursery 1'),
        (4, 'Nursery 2'),
        (5, 'Reception Year'),
        (6, 'Primary 1'),
        (7, 'Primary 2'),
        (8, 'Primary 3'),
        (9, 'Primary 4'),
        (10, 'Primary 5'),
        (11, 'JSS 1'),
        (12, 'JSS 2'),
        (13, 'JSS 3'),
        (14, 'SS 1'),
        (15, 'SS 2'),
        (16, 'SS 3')
    )
    select_class = forms.ChoiceField(choices=class_select, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Class'}))