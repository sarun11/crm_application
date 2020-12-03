from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name="accounts"),
    path('register/', views.register, name="register")   
]
