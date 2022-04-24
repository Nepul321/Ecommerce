from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import (
    Order
)

from .serializers import (
    OrderSerializer
)

@api_view(["GET"])
def OrdersView(request, *args, **kwargs):
    return Response({"detail" : "orders"}, status=200)

@api_view(["GET"])
def OrderItemsView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=user, complete=False)
        serializer = OrderSerializer(order)
        data = serializer.data
    else:
        data = {}



    return Response(data, status=200)