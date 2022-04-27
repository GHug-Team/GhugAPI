from rest_framework import routers
from .views import  ArticleViewset


router = routers.DefaultRouter()
router.register('api/articles', ArticleViewset)