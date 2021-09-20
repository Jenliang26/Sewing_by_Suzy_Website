from django.urls import path
from orders import views

urlpatterns = [
    path('', views.OrderView.as_view()),
    path('detail/<int:pk>/', views.OrderDetail.as_view()),
    path('garment/', views.GarmentList.as_view()),
    path('garment/<int:orderpk>/', views.GarmentList.as_view())
]