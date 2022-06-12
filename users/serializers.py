from rest_framework import serializers
from users.models import CustomUser , Baby
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id','email', 'user_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        
        instance.save()
        return instance
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)  
    password = serializers.CharField(min_length=8, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials Passed.')

class BabySerializer (serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = ( 'id','name', 'img', 'birthdate', 'height', 'weight', 'gender', 'relationship', 'user' )