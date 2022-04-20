from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def APIBasePoint(request, *args, **kwargs):
    return Response({"detail" : "API BASE POINT"}, status=200)