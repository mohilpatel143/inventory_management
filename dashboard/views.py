import dashboard
from typing import SupportsAbs
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Supplier
from .forms import ProductForm, OrderForm, SupplierForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required
def index(request):
    orders = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()        
    context = {
        'orders': orders,
        'form':form,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    dealers_count = Supplier.objects.all().count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'workers': workers,
        'workers_count': workers_count,
        'dealers_count': dealers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/staff.html', context)   

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk) 
    context={
        'workers': workers,
        
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required
def supplier(request):
    dealers = Supplier.objects.all()
    dealers_count = dealers.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()

    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            supplier_name = form.cleaned_data.get('supplier_name')
            messages.success(request, f'{supplier_name} has been added')
            return redirect('dashboard-supplier')
    else:
        form = SupplierForm()    
    context = {
        'dealers': dealers,
        'form': form,
        'dealers_count': dealers_count,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/supplier.html', context)   

def supplier_delete(request, pk):
    dealer = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        dealer.delete()
        return redirect('dashboard-supplier')
    return render(request, 'dashboard/supplier_delete.html')    

def supplier_update(request, pk):
    dealer = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=dealer)
        if form.is_valid():
            form.save()
            return redirect('dashboard-supplier')
    else:
        form = SupplierForm(instance=dealer)    

    context={
        'form':form,
    }
    return render(request, 'dashboard/supplier_update.html', context)

@login_required
def product(request):
    items = Product.objects.all() # using ORM
    product_count = items.count()
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    dealers_count = Supplier.objects.all().count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('product_name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()    
    context={
        'items' : items,
        'form' : form, 
        'product_count': product_count,
        'dealers_count': dealers_count,
        'workers_count': workers_count,
        'orders_count': orders_count,
    }
    return render(request, 'dashboard/product.html', context)   

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)    
    context={
        'form':form, 
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    dealers_count = Supplier.objects.all().count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    context ={
        'orders':orders,
        'orders_count': orders_count,
        'workers_count': workers_count,
        'dealers_count': dealers_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/order.html', context)   
