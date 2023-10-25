from django.shortcuts import render, HttpResponse

# Create your views here.

data = {
    'car': 'BMW',
    'computer': 'Asus',
    'tablet': 'Xiaomi',
}

def index(request):

    aletler = data

    return render(request, 'uygulama1index/index.html', {
        'aletler': aletler
    })

def detay(request):

    alet_detay = list(data.values())

    context = {
        'alet_detay': alet_detay
    }
    return render(request, 'uygulama1detaylar/detay.html', context)

def urunler(request):
    return HttpResponse('index sayfam')

def kategori_ismine_gore(request, category):
    category_text = ''
    if category == 'telefon':
        category_text = 'Telefon sayfasi'
    elif category == 'bilgisayar':
        category_text = 'Bilgisayar sayfasi'
    else:
        category_text = 'Yanlış kategori girdiniz'    
    return HttpResponse(category_text)

def kategori_id(request, category_id):
    text = ''
    if category_id == 1:
        text = 'Telefon id:1 sayfası'
    elif category_id == 2:
        text = 'Bilgisayar id:2 sayfası'
    else:
        text = 'yanlış değer'
    
    return HttpResponse(text)