from django import forms
from .models import Book, Category, Borrowed
from flatpickr import DateTimePickerInput


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'total_copies': forms.NumberInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'available_copies': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }  

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Borrowed
        fields = ('issue_date', 'return_date') 
        widgets = {
            'issue_date': DateTimePickerInput(attrs={'class': 'form-control'}),
            'return_date': DateTimePickerInput(attrs={'class': 'form-control'}),

        }     

class ReturnBookForm(forms.Form):
    return_date = forms.DateTimeField(widget=DateTimePickerInput(
        attrs = {    # input element attributes
            "class": "form-control",
        },
    ))    