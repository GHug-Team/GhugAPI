from rest_framework import routers
from .views import  AlbumViewset, VaccineViewset , StatusViewset


router = routers.DefaultRouter()
router.register('api/album', AlbumViewset)
router.register('api/vaccine', VaccineViewset)
router.register('api/watch_status', StatusViewset)