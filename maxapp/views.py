from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Coche

# Create your views here.
class CochesView(APIView):

    def get(self, request, format=None):
        coches = Coche.objects.all().values()


        return Response(coches)


