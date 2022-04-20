from .views import (
    ProductDetailView
)

from django.urls import path

urlpatterns = [
    path('<str:slug>/', ProductDetailView, name="product-detail-view"),
]
