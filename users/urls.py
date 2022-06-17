
from rest_framework import routers
from .views import  BabyViewset
from django.urls import path , include
from .views import RegisterAPI, LoginAPI , does_account_exist_view, ChangePasswordView, UpdateProfileView
from knox import views as knox_views




router = routers.DefaultRouter()
#router.register('users', UserViewset)
router.register('api/babyinfo', BabyViewset)


app_name = 'users'

urlpatterns = [
    path('api/auth/', include('knox.urls')),
    path('api/register/', RegisterAPI.as_view() , name="register"),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('check_if_account_exists/', does_account_exist_view.as_view() , name="check_if_account_exists"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name="change_password"),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),
]