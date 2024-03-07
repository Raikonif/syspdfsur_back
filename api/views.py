from .models import User, Author, Article, ArticleSlide
from rest_framework import viewsets
from .serializers import UserSerializer, AuthorSerializer, ArticleSerializer, ArticleSlideSerializer


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleSlideView(viewsets.ModelViewSet):
    serializer_class = ArticleSlideSerializer
    queryset = ArticleSlide.objects.all()
