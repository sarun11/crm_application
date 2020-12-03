from django.shortcuts import render, redirect
from products.models import Product
from .forms import OrderForm
from .models import Order
from django.utils import timezone

# Create your views here.

def products(request): 
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def create_order(request):
    
    form = OrderForm()  
    if request.method == "POST":    
        # print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'create_order.html', context)


def update_order(request, pk):    
    order = Order.objects.get(id=pk)    
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        # order.date_created = timezone.now
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}   
    return render(request, 'create_order.html', context)


def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')    
    context = {'order': order}
    return render(request, 'delete_order.html', context=context)

