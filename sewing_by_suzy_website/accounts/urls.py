from django.urls import path
from accounts import views

urlpatterns = [
    # path('', views.CustomerList.as_view()),
    path('employees/', views.Employees.as_view()),
    path('customers/', views.Customers.as_view())
]