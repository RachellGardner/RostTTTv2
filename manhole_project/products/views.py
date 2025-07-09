from django.shortcuts import render
from itertools import chain
from .models import Lyuk, Dozhdiepriemnik, VodootvodnyyLotok, TrotuarnayaPlitka, Cherepitsa

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def product_list(request):
    # Берём товары из всех категорий
    products = list(chain(
        Lyuk.objects.all(),
        Dozhdiepriemnik.objects.all(),
        VodootvodnyyLotok.objects.all(),
        TrotuarnayaPlitka.objects.all(),
        Cherepitsa.objects.all()
    ))
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    # Проверяем во всех моделях
    for model in [Lyuk, Dozhdiepriemnik, VodootvodnyyLotok, TrotuarnayaPlitka, Cherepitsa]:
        try:
            product = model.objects.get(pk=pk)
            return render(request, 'product_detail.html', {'product': product})
        except model.DoesNotExist:
            continue

    # Если не найден
    from django.http import Http404
    raise Http404("Товар не найден")