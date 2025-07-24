from django.shortcuts import render, get_object_or_404
from itertools import chain
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from .models import Lyuk, Dozhdiepriemnik, VodootvodnyyLotok, Kryshki, Koltsa, KonusnyePerehody, ProductImage

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def product_list(request):
    # Создаем список продуктов с информацией о типе
    products = []
    for model in [Lyuk, Dozhdiepriemnik, VodootvodnyyLotok, Kryshki, Koltsa, KonusnyePerehody]:
        for product in model.objects.all():
            product.model_type = model.__name__.lower()  # Добавляем тип модели к продукту
            products.append(product)
    
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, model_type, pk):
    # Определяем модель по переданному типу
    model_map = {
        'lyuk': Lyuk,
        'dozhdiepriemnik': Dozhdiepriemnik,
        'vodootvodnyylotok': VodootvodnyyLotok,
        'kryshki': Kryshki,
        'koltsa': Koltsa,
        'konusnyeperehody': KonusnyePerehody
    }
    
    model = model_map.get(model_type.lower())
    if not model:
        raise Http404("Тип продукта не найден")
    
    # Получаем продукт
    product = get_object_or_404(model, pk=pk)
    
    # Получаем дополнительные изображения
    content_type = ContentType.objects.get_for_model(model)
    additional_images = ProductImage.objects.filter(
        content_type=content_type,
        object_id=product.id
    ).order_by('created_at')
    
    return render(request, 'product_detail.html', {
        'product': product,
        'product_images': additional_images
    })