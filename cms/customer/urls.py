from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.customer, name="customers"),
    path('delete_order_/<str:cid>/<str:pk>/', views.delete_order_, name="delete_order_"),
    path('update_order_/<str:cid>/<str:pk>/', views.update_order_, name="update_order_")
]
