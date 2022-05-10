from rest_framework import routers
from .views import  AlbumViewset, VaccineViewset


router = routers.DefaultRouter()
router.register('api/album', AlbumViewset)
router.register('api/vaccine', VaccineViewset)