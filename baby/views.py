from rest_framework import viewsets
from rest_framework import permissions
from .models import Album, Vaccine
from .serializers import AlbumSerializer, VaccineSerializer

class AlbumViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


    
class VaccineViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

