from rest_framework import serializers
from . models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','title', 'desc','created_at', 'updated_at' )

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title', 'body','date', 'time','user','category','created_at', 'updated_at' )

