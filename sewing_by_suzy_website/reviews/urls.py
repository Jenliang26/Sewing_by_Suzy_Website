from django.urls import path
from reviews import views

urlpatterns = [
    path('', views.ReviewList.as_view()),
    path('detail/<int:pk>/', views.ReviewDetail.as_view())
]