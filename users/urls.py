
from rest_framework import routers
from .views import  BabyViewset
from django.urls import path
from .views import CreateCustomUser, BlacklistTokenUpdateView , MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
#router.register('users', UserViewset)
router.register('api/babyinfo', BabyViewset)


app_name = 'users'

urlpatterns = [
    path('register/', CreateCustomUser.as_view(), name="create_user"),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist'),
]