from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20).unique
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=15)
    email = models.EmailField().unique

    def __str__(self):
        return self.username + " " + self.email + " " + self.role

    class Meta:
        db_table = "users"


class Author(models.Model):
    mention = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    avatar = models.CharField(max_length=255)
    email = models.EmailField()
    twitter = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    facebook = models.CharField(max_length=40)

    def __str__(self):
        return self.mention + " " + self.full_name

    class Meta:
        db_table = "authors"


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + " / " + self.type

    class Meta:
        db_table = "articles"


class ArticleSlide(models.Model):
    url = models.CharField(max_length=255)
    description = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'articles_slides'
