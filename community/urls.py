from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from community import views


router = routers.DefaultRouter()

router.register('profile', views.ProfileViewSet)
router.register('groups', views.GroupViewSet)
router.register('discipline', views.DisciplineViewSet)
router.register('researchField', views.ResearchFieldViewSet)
router.register('researchEstablishment', views.ResearchEstablishmentViewSet)

# router.register('discipline', views.DisciplineViewSet, basename='discipline')
# router.register('researchFields', views.ResearchFieldViewSet)
# router.register('researchEstablishment', views.ResearchEstablishmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]