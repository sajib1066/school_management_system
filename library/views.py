from django.shortcuts import render, redirect
from .models import Book, Borrowed
from .forms import BookForm, CategoryForm, BorrowBookForm, ReturnBookForm
from django.contrib import messages
from student.forms import SearchEnrolledStudentForm
from student.models import EnrolledStudent, PersonalInfo
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def AddBook(request):
    form = BookForm
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Book Added Successfully')
            return redirect('home')        
    context = {
        'form': form,
    }
    return render(request, 'library/add-book.html', context)

@login_required(login_url='login')
def AddCategory(request):
    form = CategoryForm
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Book Added Successfully')
            return redirect('home')        
    context = {
        'form': form,
    }
    return render(request, 'library/add-category.html', context)    

@login_required(login_url='login')
def ListBooks(request):
    books = Book.objects.all()
    context = {
        'books': books
    }    
    return render(request, 'library/view-books.html', context)

@login_required(login_url='login')
def ViewBook(request, id):
    book = Book.objects.get(id=id)
    borrowers = Borrowed.objects.filter(book__id=id, returned=False)
    context = {
        'book': book,
        'borrowers': borrowers
    }  
    return render(request, 'library/view-book.html', context)

@login_required(login_url='login')
def BorrowBook(request, id):
    book = Book.objects.get(id=id)
    form = SearchEnrolledStudentForm()
    borrowform = BorrowBookForm()
    class_name = request.GET.get('reg_class', None)
    students = None
    if class_name:
        students = EnrolledStudent.current_year.filter(class_name=class_name)
    if request.method == 'POST':
        bform = BorrowBookForm(request.POST)
        student = request.POST['studentname']
        student = PersonalInfo.objects.get(name=student)
        if bform.is_valid() and book.available_copies >= 1:
            form = bform.save(commit=False)
            form.student = student
            form.book = book
            book.available_copies = book.available_copies - 1
            book.save()
            form.save()
            messages.info(request, 'Book Borrowing Approved')
            return redirect('view-books')
        else:
            messages.info(request, "Book isn't available") 
            return redirect('view-books')      
    context = {
        'form': form,
        'book': book,
        'students': students,
        'borrowform': borrowform
    }
    return render(request, 'library/borrow-book.html', context)

@login_required(login_url='login')
def ReturnBook(request, id):
    borrow = Borrowed.objects.get(id=id)
    form = ReturnBookForm()
    if request.method == 'POST':
        form = ReturnBookForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['return_date']
            borrow.returned = True
            borrow.return_date = date
            BB = Book.objects.get(id=borrow.book.id)
            BB.available_copies += 1
            BB.save()
            borrow.save()
            messages.info(request, 'Book returned successfully')
            return redirect('home')

    context = {
        'borrow': borrow,
        'form': form,
    }
    return render(request, 'library/return-book.html', context)


@login_required(login_url='login')
def EditBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book edited successfully')
            return redirect('home')
    form = BookForm(instance=book)
    context = {
        'form': form
    }    
    return render(request, 'library/edit-book.html', context)

