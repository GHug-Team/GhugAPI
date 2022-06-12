from rest_framework import status
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly  
from rest_framework import viewsets
from .models import CustomUser , Baby
from .serializers import CustomUserSerializer , BabySerializer ,LoginSerializer
from knox.models import AuthToken
from rest_framework import generics


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
        
       
     
		

def validate_email(email):
	account = None
	try:
		account = CustomUser.objects.get(email=email)
	except account.DoesNotExist:
		return None
	if account != None:
		return email


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




class BabyViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    queryset = Baby.objects.all()
    serializer_class = BabySerializer




"""
class CreateCustomUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                token = AuthToken.objects.create(user)[1] 
                return Response(json, token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
"""


