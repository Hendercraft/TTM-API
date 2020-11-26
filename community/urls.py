from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from community import views


router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

router.register('discipline', views.DisciplineViewSet, basename='discipline')
router.register('researchFields', views.ResearchFieldViewSet)
router.register('researchEstablishment', views.ResearchEstablishmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/extra/discipline/', views.DisciplineViewSet.as_view({'get':'list'})),
    path('users/extra/researchfields/', views.ResearchFieldViewSet.as_view({'get':'list'})),
    path('users/extra/researchestablishment/', views.ResearchEstablishmentViewSet.as_view({'get':'list'})),
]