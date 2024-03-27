from django.urls import path
from . import views

urlpatterns = [
    path('', views.datasets, name="datasets"),
    path('dataset/<str:pk>/', views.dataset, name="dataset"),
]
