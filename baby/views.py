from rest_framework import viewsets
from rest_framework import permissions
from .models import Album, Vaccine , WatchStatus
from .serializers import AlbumSerializer, VaccineSerializer , WatchStatusSerializer

class AlbumViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


    
class VaccineViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer


class StatusViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = WatchStatus.objects.all()
    serializer_class = WatchStatusSerializer