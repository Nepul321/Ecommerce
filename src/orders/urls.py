from django.urls import path
from .api.views import (
    OrderItemsView,
    OrdersView
)

urlpatterns = [
    path('', OrdersView, name="orders"),
    path('cart/', OrderItemsView, name="cart"),
]
