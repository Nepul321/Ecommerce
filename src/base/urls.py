from .views import (
    HomeView
)

from .api.views import (
    APIBasePoint
)

from django.urls import path

urlpatterns = [
    path('', HomeView, name="home"),
    path('api/', APIBasePoint, name="api-base-point"),
]
