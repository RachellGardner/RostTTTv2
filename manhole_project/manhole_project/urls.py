from django.contrib import admin
from django.urls import path, include
from products import views  # Явный импорт views из приложения products
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('products.urls')),  # Подключение других URL
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)