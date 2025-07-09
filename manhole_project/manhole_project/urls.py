from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
       path('catalog/manholes/', views.manholes_catalog, name='manholes-catalog'),
    path('catalog/inspection-chambers/', views.inspection_chambers, name='inspection-chambers'),
    path('catalog/drainage/', views.drainage, name='drainage'),
    path('catalog/channels/', views.channels, name='channels'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)