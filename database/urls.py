from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from database import views


router = routers.DefaultRouter()

router.register('dates', views.DateViewSet)
router.register('qualities', views.QualityViewSet)
router.register('sourceType', views.SourceTypeViewSet)
router.register('authors', views.AuthorViewSet)
router.register('contents', views.ContentViewSet)
router.register('urls', views.UrlViewSet)
router.register('sources', views.SourceViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('search/', views.Search, name='search')
]