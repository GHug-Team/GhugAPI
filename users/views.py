from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly , AllowAny , IsAuthenticated
from rest_framework import viewsets
from .models import CustomUser , Baby
from .serializers import CustomUserSerializer , BabySerializer ,LoginSerializer, UpdateUserSerializer,ChangePasswordSerializer
from knox.models import AuthToken
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
#register
class RegisterAPI(generics.GenericAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        



#login
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
"""
class LoggedInUserView(APIView):
    def get(self, request):
        serializer = CustomUserSerializer(self.request.user)
        return Response({"user": serializer.data, "token":AuthToken.objects.get(token=token)
        
        })
"""
class UserViewSet(viewsets.ViewSet):
    
    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomUserSerializer(user)
        return Response({"user": serializer.data, "token":AuthToken.objects.create(user)[1]})
    


class does_account_exist_view(APIView):
    
    def post(self, request):
        email = request.data['email']
        is_already_exists = CustomUser.objects.filter(email=email).exists()
        res= {"response": is_already_exists}
        return Response (res)


class BabyViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    parser_classes = (MultiPartParser, FormParser)
    queryset = Baby.objects.all()
    serializer_class = BabySerializer





class ChangePasswordView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer