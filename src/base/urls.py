from .views import (
    HomeView,
    ProductView
)

from .api.views import (
    APIBasePoint
)

from django.urls import path

urlpatterns = [
    path('', HomeView, name="home"),
    path('api/', APIBasePoint, name="api-base-point"),
    path('products/<int:id>/', ProductView, name="product"),
]
