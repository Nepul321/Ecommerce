from django.urls import path
from .api.views import (
    ShippingView
)

urlpatterns = [
    path('', ShippingView, name="shipping-home"),
]
