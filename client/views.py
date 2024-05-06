from client.models import Client
from client.serializers import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status']
    ordering_fields = ['name']
    queryset = Client.objects.all()
    search_fields = ['name', 'rg', 'cpf', 'email', 'phone']
    serializer_class = ClientSerializer