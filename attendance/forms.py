from django import forms
from academic.models import ClassRegistration
from flatpickr import DatePickerInput

class SearchEnrolledStudentForm(forms.Form):
    reg_class = forms.ModelChoiceField(queryset=ClassRegistration.objects.all())

class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)

class AttendanceForm(forms.Form):
    mark_attendance = forms.ChoiceField(widget=forms.RadioSelect, choices=class_attendance)

class DateForm(forms.Form):
    date = forms.DateField(widget=DatePickerInput())
