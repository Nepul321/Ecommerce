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