from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .serializers import DirectionSerializer, SuccursaleSerializer, ClientSerializer, AssuranceSerializer
from .models import Direction, Succursale, Client, Assurance

class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class SuccursaleViewSet(viewsets.ModelViewSet):
    queryset = Succursale.objects.all()
    serializer_class = SuccursaleSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AssuranceViewSet(viewsets.ModelViewSet):
    queryset = Assurance.objects.all()
    serializer_class = AssuranceSerializer
