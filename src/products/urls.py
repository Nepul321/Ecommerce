# from .views import (
#     ProductDetailView
# )

from .api.views import (
    ProductsView,
    ProductDetailView
)

from django.urls import path

urlpatterns = [
    # path('<int:id>/', ProductDetailView, name="product-detail-view"),
    path('', ProductsView, name="products-list"),
    path('<int:id>/', ProductDetailView, name="product-details")
]
