from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from customer.models import Customer
from products.models import Order
from django.db.models import Q

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    total_orders = orders.count()
    
    last_5 = Order.objects.all().order_by('-date_created')[:5]
    
    orders_delivered = Order.objects.filter(status='Delivered').count()
    orders_pending = Order.objects.filter(~Q(status='Delivered')).count()
    
    return render(request, "home.html", 
                  {'customer': customers, 
                   'orders': orders, 
                   'total_orders': total_orders,
                   'orders_delivered': orders_delivered,
                   'orders_pending': orders_pending,
                   'last_5': last_5,
                   })
