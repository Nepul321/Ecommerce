from .views import (
    ProductDetailView
)

from django.urls import path

urlpatterns = [
    path('<int:id>/', ProductDetailView, name="product-detail-view"),
]
