from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.CustomerList.as_view()),
    path('', views.EmployeeList.as_view())
]