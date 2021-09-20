from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryView.as_view()),
    path('item/<int:pk>/', views.Item_Query.as_view())

]
