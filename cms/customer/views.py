from django.shortcuts import render
from customer.models import Customer
# Create your views here.

def customer(request, pk):
    
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    
    total_orders = orders.count()
    
    context = {'customer': customer, 'total_orders': total_orders, 'orders': orders}
    return render(request, 'customer.html', context)
