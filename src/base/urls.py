from .views import (
    HomeView,
    ProductView,
    CartView,
    SearchView
)

from .api.views import (
    APIBasePoint
)

from django.urls import path

urlpatterns = [
    path('', HomeView, name="home"),
    path('api/', APIBasePoint, name="api-base-point"),
    path('products/<int:id>/', ProductView, name="product"),
    path('cart/', CartView, name="cart-view"),
    path('search/', SearchView, name="search")
]
