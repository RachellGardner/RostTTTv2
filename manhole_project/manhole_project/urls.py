from django.contrib import admin
from django.urls import path, include
from products import views  # Явный импорт views из приложения products

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('products.urls')),  # Подключение других URL
]
