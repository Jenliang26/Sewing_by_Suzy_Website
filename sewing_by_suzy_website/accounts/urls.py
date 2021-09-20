from django.urls import path
from accounts import views

urlpatterns = [
    # path('', views.CustomerList.as_view()),
    path('employees/', views.Employees.as_view()),
    path('customers/', views.Customers.as_view()),
    path('customers/<int:pk>/', views.Customers.as_view()),
    path('customers/user/<int:uid>/', views.Customer_By_User.as_view()),
    path('employees/user/<int:uid>/', views.Employee_By_User.as_view())
]