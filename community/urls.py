from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from community import views


router = routers.DefaultRouter()

router.register('profile', views.ProfileViewSet, basename='Profile')
#router.register('groups', views.GroupViewSet)
router.register('discipline', views.DisciplineViewSet)
router.register('researchField', views.ResearchFieldViewSet)
router.register('researchEstablishment', views.ResearchEstablishmentViewSet)

# router.register('discipline', views.DisciplineViewSet, basename='discipline')
# router.register('researchFields', views.ResearchFieldViewSet)
# router.register('researchEstablishment', views.ResearchEstablishmentViewSet)

urlpatterns = [
    # path('', include(router.urls)),

    #User profile
    path('', views.ListProfile.as_view()),
    path('user/', views.ListUser.as_view()),
    path('create/', views.CreateProfile.as_view()),
    path('<int:pk>/', views.RetrieveProfile.as_view()),
    path('update/<int:pk>/', views.UpdateProfile.as_view()),

    #Discipline
    path('discipline/', views.DisciplineViewSet.as_view({'get':'list'})),
    path('discipline/create/', views.DisciplineViewSet.as_view({'post':'create'})),
    path('discipline/<int:pk>/', views.DisciplineViewSet.as_view({'get':'retrieve'})),
    path('discipline/update/<int:pk>/', views.DisciplineViewSet.as_view({'put': 'update'})),

    #Research Fields
    path('researchField/', views.ResearchFieldViewSet.as_view({'get':'list'})),
    path('researchField/create/', views.ResearchFieldViewSet.as_view({'post':'create'})),
    path('researchField/<int:pk>/', views.DisciplineViewSet.as_view({'get':'retrieve'})),
    path('researchField/update/<int:pk>/', views.ResearchFieldViewSet.as_view({'put': 'update'})),

    #Research Establishment
    path('researchEstablishment/', views.ResearchEstablishmentViewSet.as_view({'get':'list'})),
    path('researchEstablishment/create/', views.ResearchEstablishmentViewSet.as_view({'post':'create'})),
    path('researchEstablishment/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'get':'retrieve'})),
    path('researchEstablishment/update/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'put': 'update'})),
]