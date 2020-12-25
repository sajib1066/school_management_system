from django import forms
from .models import *
from academic.models import ClassRegistration
from flatpickr import DatePickerInput

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
class AddFeeForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3 digit unique fee code'}), 
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),           
        }    

class AddDiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3 digit unique discount code'}), 
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount in percentages'}),           
        }    


class SelectClassForm(forms.Form):
    classes = forms.MultipleChoiceField(choices=class_select, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))  
    fee = forms.ModelChoiceField(queryset=Fees.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class StudentFeeForm(forms.Form):
    fee = forms.ModelChoiceField(queryset=Fees.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class StudentPaidFeeForm(forms.ModelForm):
    class Meta:
        model = StudentFeesPaid
        fields = ['amount', 'date']
        widgets = {
            'date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount paid'}),           
        }    

class StudentDiscountForm(forms.Form):
    discount = forms.ModelChoiceField(queryset = Discount.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class StudentIDForm(forms.Form):
    reg_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'palceholder': 'Student registration number'}))