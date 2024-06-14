from django.urls import path
from . import views

urlPatterns = [
    path('', views.hello),
    path('about/', views.about),
]