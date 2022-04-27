from rest_framework import routers
from .views import  CategoryViewset, TaskViewset


router = routers.DefaultRouter()
router.register('api/reminderCategory', CategoryViewset)
router.register('api/reminderTask', TaskViewset)
