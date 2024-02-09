from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20).unique
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=15)
    email = models.EmailField().unique


class Author(models.Model):
    mention = models.CharField(max_length=20)
    fullname = models.CharField(max_length=100)
    email = models.EmailField().unique
    twitter = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    facebook = models.CharField(max_length=40)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    url = models.CharField(max_length=255)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
