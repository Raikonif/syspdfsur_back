from django.contrib import admin
from .models import User, Author, Article, ArticleSlide
# Register your models here.

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(ArticleSlide)
