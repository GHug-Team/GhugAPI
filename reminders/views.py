from rest_framework import viewsets
from rest_framework import permissions
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


class TaskViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    