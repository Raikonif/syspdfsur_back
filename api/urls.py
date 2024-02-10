from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(prefix=r"users", viewset=views.UserView, basename="users")
router.register(prefix=r"authors", viewset=views.AuthorView, basename="authors")
router.register(prefix=r"articles", viewset=views.ArticleView, basename="articles")
router.register(prefix=r"images", viewset=views.ImageView, basename="images")

urlpatterns = [
    path("v1/", include(router.urls)),
]
