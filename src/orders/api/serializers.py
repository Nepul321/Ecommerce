from rest_framework import serializers
from ..models import (
    Order,
    OrderItem
)

from base.api.serializers import UserSerializer
from products.api.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'date_added')

class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    cart_total = serializers.SerializerMethodField(read_only=True)
    cart_items = serializers.SerializerMethodField(read_only=True)
    shipping = serializers.SerializerMethodField(read_only=True)
    order_items = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'date_ordered', 'complete', 'transaction_id', 'cart_total', 'cart_items', 'shipping', 'order_items')

    def get_cart_total(self, obj):
        total = obj.get_cart_total
        return total

    def get_cart_items(self, obj):
        total = obj.get_cart_items
        return total

    def get_shipping(self, obj):
        shipping = obj.shipping
        return shipping

    def get_order_items(self, obj):
        orderitems = obj.orderitem_set.all()
        serializer = OrderItemSerializer(orderitems, many=True)
        return serializer.data