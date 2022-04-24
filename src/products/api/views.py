from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Product
from .serializers import (
    ProductSerializer
)

@api_view(['GET'])
def ProductsView(request, *args, **kwargs):
    qs = Product.objects.all()
    serializer = ProductSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)

@api_view(['GET'])
def ProductDetailView(request, id, *args, **kwargs):
    qs = Product.objects.filter(id=id)
    if not qs:
        return Response({"detail" : "Product not found"}, status=404)
    obj = qs.first()
    serializer = ProductSerializer(obj)
    data = serializer.data
    return Response(data, status=200)