from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from community import views


router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('users/<int:pk>/Discipline', views.DisciplineViewSet)
router.register('users/<int:pk>/ResearchFields', views.ResearchFieldViewSet)
router.register('users/<int:pk>/ResearchEstablishment', views.ResearchEstablishmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]