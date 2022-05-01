from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from ..models import (
    Order,
    OrderItem
)

from .serializers import (
    OrderSerializer,
    OrderItemSerializer
)

from shipping.models import ShippingAddress

import datetime

from products.models import Product

from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
def OrdersView(request, *args, **kwargs):
    return Response({"detail" : "orders"}, status=200)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def OrderItemsView(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=user, complete=False)
        serializer = OrderSerializer(order)
        data = serializer.data
    else:
        data = {}



    return Response(data, status=200)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def AddToCartView(request, *args, **kwargs):
    data = request.data
    user = request.user
    order, created = Order.objects.get_or_create(customer=user, complete=False)
    
    product_id = data['id']
    action = data['action']

    qs = Product.objects.filter(id=product_id)
    if not qs:
        return Response({"detail" : "Product not found"}, status=404)
    obj = qs.first()

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=obj)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    serializer = OrderSerializer(order)
    data = serializer.data
    
    return Response(data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CheckoutView(request, *args, **kwargs):
    transaction_id = datetime.datetime.now().timestamp()
    data = request.data
    customer = request.user
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = data['total']
    order.transaction_id = transaction_id

    if float(total) == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
            ShippingAddress.objects.create(
                 
                 customer=customer,
                 country=data['country'],
                 order=order,
                 address=data['address'],
                 city=data['city'],
                 state=data['state'],
                 zipcode=data['zipcode'],
                )
            return Response({"detail" : "Payment completed"}, status=200)
    else:
        return Response({"detail" : "Payment completed"}, status=200)