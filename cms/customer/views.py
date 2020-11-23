from django.shortcuts import render, redirect
from customer.models import Customer
from products.models import Order
from products.forms import OrderForm

# Create your views here.

def customer(request, pk):
    
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    
    total_orders = orders.count()
    
    context = {'customer': customer, 'total_orders': total_orders, 'orders': orders}
    return render(request, 'customer.html', context)


def delete_order_(request, cid, pk):
    
    customer = Customer.objects.get(id=cid)
    order = Order.objects.get(id=pk)
     
    if request.method == 'POST':
        order.delete()
        path = '/customer/' + str(cid) + '/'
        return redirect(path)
          
    context = {'order': order, 'customer': customer} 
    return render(request, 'delete_order_customer.html', context=context)


def update_order_(request, cid, pk):
    
    customer = Customer.objects.get(id=cid)
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            path = '/customer/' + str(cid) + '/'
            return redirect(path)
        
    context = {'customer': customer, 'order': order, 'form': form}
    
    return render(request, 'create_order.html', context=context)
