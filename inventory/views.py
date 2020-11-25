from django.shortcuts import render, redirect
from .models import *
from .forms import CategoryForm, AddItemForm, IssueItemForm, ReturnItemForm, CategoryItemForm, AssignItemForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def AddCategory(request):
    form = CategoryForm
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Category Added Successfully')
            return redirect('add-inventory-category')
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'inventory/add-category.html', context)

@login_required(login_url='login')
def DeleteCategory(request):
    if request.method == 'POST':
        id = request.POST['id']
        try:
            Category.objects.get(id=id).delete()
            messages.info(request, 'Successfully deleted Category')
        except:
            messages.info(request, 'Could not delete Category')    
        return redirect('add-inventory-category')

@login_required(login_url='login')
def AddItem(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Item Added Successfully')
    context = {
        'form': form,
    }        
    return render(request, 'inventory/add-item.html', context)

@login_required(login_url='login')
def ViewItems(request):
    form = CategoryItemForm()
    cat = request.GET.get('category', None)
    if cat:
        items = Item.objects.filter(category=cat)
    else:
        items = Item.objects.all()
    context = {
        'form': form,
        'items': items,
    }
    return render(request, 'inventory/view-items.html', context)

@login_required(login_url='login')
def ViewItem(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item
    }    
    return render(request, 'inventory/view-item.html', context)

@login_required(login_url='login')
def IssueItem(request):
    form = IssueItemForm()
    if request.method == 'POST':
        form = IssueItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'form saved successfully')
            redirect('issue-inventory-item')
    issued= Issued.objects.filter(returned=False).order_by('issue_date')
    context = {
        'form': form,
        'issued': issued
    }    
    return render(request, 'inventory/issue-item.html', context)  

@login_required(login_url='login')
def ReturnItem(request, id):
    issued = Issued.objects.get(id=id)
    form = ReturnItemForm(instance=issued)
    if request.method == 'POST':
        form1 = ReturnItemForm(request.POST, instance=issued)
        if form1.is_valid():
            form = form1.save(commit=False)
            form.returned = True
            messages.info(request, 'Item returned successfully')
            return redirect('issue-inventory-item')
    context = {
        'issued': issued,
        'form': form
    }
    return render(request, 'inventory/return-item.html', context)

@login_required(login_url='login')
def AssignItem(request, id):
    item = Item.objects.get(id=id)
    form = AssignItemForm()
    if request.method == 'POST':
        form = AssignItemForm(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.item = item 
            form1.save()
            messages.info(request, 'Class Item assigned successfully')
            return redirect('issue-inventory-item')
    context = {
        'item': item,
        'form': form
    }
    return render(request, 'inventory/assign-item.html', context) 

@login_required(login_url='login')
def AssignedItems(request):
    items = ClassItems.objects.all().order_by('class_name')
    context = {
        'items': items,
    }
    return render(request, 'inventory/view-assigned-items.html', context)


@login_required(login_url='login')
def StudentsAssigned(request, id):
    item = ClassItems.objects.get(id=id)
    if request.method == 'POST':
        try:
            id =  request.POST['id']
            student = EnrolledStudent.objects.get(id=id)
            StudentItems.objects.create(classs=item, students_given=student)
            messages.info(request, 'Student given item added successfully')
        except:
            messages.error(request, "Couldn't perform action")    

    students_given = StudentItems.objects.filter(classs=item)
    not_given = EnrolledStudent.current_year.filter(class_name__class_name=item.class_name).exclude(id__in=students_given.values('students_given'))
    context = {
        'item': item,
        'students_given': students_given,
        'not_given': not_given
    }
    return render(request, 'inventory/student-class-items.html', context)



