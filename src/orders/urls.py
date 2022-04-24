from django.urls import path
from .api.views import (
    OrderItemsView,
    OrdersView,
    AddToCartView
)

urlpatterns = [
    path('', OrdersView, name="orders"),
    path('cart/', OrderItemsView, name="cart"),
    path('cart/add/', AddToCartView, name="card-add"),
]
