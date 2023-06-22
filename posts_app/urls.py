from django.urls import path
from posts_app import views
urlpatterns = [
    path("", views.ApiOverview, name="home"),
    ]
