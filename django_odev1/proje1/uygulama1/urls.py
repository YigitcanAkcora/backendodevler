from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_sayfasi'),
    path('detay/', detay, name='detay_sayfasi'),
    path('urunler/', urunler, name='urunler_sayfasi'),
    path('<int:category_id>/', kategori_id),
    path('<str:category>/', kategori_ismine_gore),
]
