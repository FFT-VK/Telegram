from django.urls import path
from . import views

urlpatterns = [
    path('telegram/<str:contact>/', views.index, name='index'),
]