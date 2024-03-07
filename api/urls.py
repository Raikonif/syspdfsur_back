from django.urls import path, include
from rest_framework import routers
from api import views
# for swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(prefix=r"users", viewset=views.UserView, basename="users")
router.register(prefix=r"authors", viewset=views.AuthorView, basename="authors")
router.register(prefix=r"articles", viewset=views.ArticleView, basename="articles")
router.register(prefix=r"articles_slides", viewset=views.ArticleSlideView, basename="articles_slides")

schema_view = get_schema_view(
    openapi.Info(
        title="SysPDFSur API",
        default_version="v1",
        description="Api for SysPDFSur",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="raikonif@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name='schema-swagger-ui'),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name='schema-redoc'),
]
