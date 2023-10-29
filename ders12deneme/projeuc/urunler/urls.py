from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_page'),
    path('<str:kategori>/', filtre, name='filtre_page'),
]
