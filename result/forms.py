from django import forms
from .models import SubjectRegistration, ClassRegistration, Result, StudentResult
from academic.models import Session

class SubjectRegistrationForm(forms.ModelForm):
    class Meta:
        model = SubjectRegistration
        fields = '__all__'

        widgets = {
            'select_class': forms.Select(attrs={'class': 'form-control'}),
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'pass_mark': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'periods_per_week': forms.NumberInput(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'})
        }

class ClassSelectSubjectListForm(forms.Form):
    select_class = forms.ModelChoiceField(queryset=ClassRegistration.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class ClassSelectMarkEntryForm(forms.Form):
    select_class = forms.ModelChoiceField(queryset=ClassRegistration.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    select_subject = forms.ModelChoiceField(queryset=SubjectRegistration.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class StudentResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('__all__') 
        widgets ={
            'student': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'test_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'exam_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }   

class ResulltForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('test_score', 'exam_score', 'total_score')
        widgets = {
            'test_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'exam_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ApprovalForm(forms.Form):
    approve = forms.BooleanField()  

class TeacherResultsForm(forms.Form):
    teacher_comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    principal_comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))