from rest_framework import viewsets
from rest_framework import permissions
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    