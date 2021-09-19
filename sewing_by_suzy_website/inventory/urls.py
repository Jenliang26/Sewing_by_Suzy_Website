from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.InventoryList.as_view()),
    path('detail/', views.InventoryDetail.as_view())
]
