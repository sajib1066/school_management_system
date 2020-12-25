from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Item, Category
from .forms import *
from django.contrib import messages
from django.utils import timezone
from account.decorators import student_required, teacher_required
from django.views.decorators.http import require_POST

# Create your views here.

@login_required(login_url='login')
def ViewStore(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'store/home-page.html', context)

@login_required(login_url='login')
def ViewStoreCategory(request, name):
    categories = Category.objects.all()
    items = Item.objects.filter(category__name=name)
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'store/home-page.html', context)

@login_required(login_url='login')
def ViewStoreItem(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'store/product-page.html', context)  

@login_required(login_url='login')
def AddStoreItem(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Item Added Successfully')
            return redirect('add-store-item')
    context = {
        'form': form
    }    
    return render(request, 'store/add-store-item.html', context)

@login_required(login_url='login')
def AddStoreCategory(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Store Category added successfully')
    context = {
        'form': form
    }
    return render(request, 'store/add-store-category.html', context)

@login_required(login_url='login')
def ViewCheckout(request):
    order = Order.objects.get(user=request.user, ordered=False)
    context = {
        'order': order,
    }   
    return render(request, 'store/checkout-page.html', context)

@login_required(login_url='login')
def add_to_cart(request):
    if request.method == 'POST':
        id = request.POST['id']
    else:
        messages.error(request, 'Could not perform action')
        redirect('home')    
    item = get_object_or_404(Item, id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("view-store-item", id=id)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("view-store-item", id=id)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("view-store-item", id=id)    

@login_required(login_url='login')
def remove_from_cart(request):
    if request.method == 'POST':
        id = request.POST['id']
    else:
        messages.error(request, 'Could not perform action')
        return redirect('home')    
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("view-store-item", id=id)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("view-store-item", id=id)     

@login_required(login_url='login')
def OrderSummary(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
    except ObjectDoesNotExist:
        messages.error(request, 'You do not have an active Order')
        return redirect('/')
    context = {
        'order': order
    }    
    return render(request, 'store/order-summary.html', context)    


@require_POST
@login_required(login_url='login')
def PaystackResponse(request):
    pass