from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Product
from .serializers import (
    ProductSerializer
)
from django.db.models import Q

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

@api_view(['GET'])
def SearchView(request, *args, **kwargs):
    query = request.GET.get("q")
    if not query:
        return Response({"detail" : "Nothing searched"}, status=400)
    qs = Product.objects.filter(title__contains=query)
    serializer = ProductSerializer(qs, many=True)
    data = serializer.data
    return Response(data, status=200)