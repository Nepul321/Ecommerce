from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def ShippingView(request, *args, **kwargs):
    return Response({"detail" : "Shipping"}, status=200)