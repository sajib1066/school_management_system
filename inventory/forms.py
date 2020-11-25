from django import forms
from . import models
from .models import Category, Issued, ClassItems
from flatpickr import DateTimePickerInput, DatePickerInput


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'})
        }

class AddItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'available_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'expiry_years': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CategoryItemForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())   


class IssueItemForm(forms.ModelForm):
    class Meta:
        model = Issued
        fields = ['individual', 'item', 'issue_date', 'return_date', 'quantity']
        widgets = {
            'individual': forms.TextInput(attrs={'class': 'form-control'}),
            'item': forms.Select(attrs={'class': 'form-control'}),
            'issue_date': DateTimePickerInput(attrs={'class': 'form-control'}),
            'return_date': DateTimePickerInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }    

class ReturnItemForm(forms.ModelForm):
    class Meta:
        model = Issued
        fields = ['returned_date', 'comment', 'damaged']
        widgets = {
            'returned_date': DatePickerInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AssignItemForm(forms.ModelForm):
    class Meta:
        model = ClassItems
        fields = ['class_name']
        widgets = {
            'class_name': forms.Select(attrs={'class': 'form-control'}),
        }        