from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    #* Ürün modeline kaydettiğimiz bütün ürünleri getirir
    urunler = Urun.objects.all()

    context = {
        'urunler': urunler
    }

    return render(request, 'index.html', context) 

def filtre(request, kategori):

    urunler2 = Urun.objects.filter(urun_kategorisi = kategori).values()


    return render(request, 'filtre.html',{
        'urunler2': urunler2
    })
