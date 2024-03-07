from rest_framework import serializers
from .models import User, Author, Article, ArticleSlide


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSlide
        fields = "__all__"
