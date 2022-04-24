from django.contrib import admin
from django.conf import settings
from .settings import MEDIA_ROOT
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)