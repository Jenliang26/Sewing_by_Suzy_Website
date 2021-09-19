from django.urls import path
from orders import views

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('detail/', views.OrderDetail.as_view()),
    path('garment/list/', views.GarmentList.as_view())
]