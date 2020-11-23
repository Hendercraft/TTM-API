from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from users import views


router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]