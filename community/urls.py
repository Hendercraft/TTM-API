from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from community import views


# router = routers.DefaultRouter()

# router.register('profile', views.ProfileViewSet, basename='Profile')
#router.register('groups', views.GroupViewSet)
# router.register('discipline', views.DisciplineViewSet)
# router.register('researchField', views.ResearchFieldViewSet)
# router.register('researchEstablishment', views.ResearchEstablishmentViewSet)

# router.register('discipline', views.DisciplineViewSet, basename='discipline')
# router.register('researchFields', views.ResearchFieldViewSet)
# router.register('researchEstablishment', views.ResearchEstablishmentViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    
    #User profile
    path('', views.ListProfile.as_view(), name='list-users-profile'),
    # path('user/', views.ListUser.as_view(), name='list-users'),
    path('create/', views.CreateProfile.as_view(), name='create-user-profile'),
    path('<int:pk>/', views.ProfileView.as_view(), name='retrieve-user-profile'),
    path('update/<int:pk>/', views.ProfileView.as_view(), name='update-user-profile'),
    path('delete/<int:pk>/', views.ProfileView.as_view(), name='delete-user-profile'),

    #Discipline
    path('discipline/', views.DisciplineViewSet.as_view({'get':'list'}), name='list-discipline'),
    path('discipline/create/', views.DisciplineViewSet.as_view({'post':'create'}), name='create-discipline'),
    path('discipline/<int:pk>/', views.DisciplineViewSet.as_view({'get':'retrieve'}), name='retrieve-discipline'),
    path('discipline/update/<int:pk>/', views.DisciplineViewSet.as_view({'put': 'update'}), name='update-discipline'),
    path('discipline/delete/<int:pk>/', views.DisciplineViewSet.as_view({'delete': 'destroy'}), name='delete-discipline'),

    #Research Fields
    path('researchField/', views.ResearchFieldViewSet.as_view({'get':'list'}), name='list-research-field'),
    path('researchField/create/', views.ResearchFieldViewSet.as_view({'post':'create'}), name='create-research-field'),
    path('researchField/<int:pk>/', views.ResearchFieldViewSet.as_view({'get':'retrieve'}), name='retrieve-research-field'),
    path('researchField/update/<int:pk>/', views.ResearchFieldViewSet.as_view({'put': 'update'}), name='update-research-field'),
    path('researchField/delete/<int:pk>/', views.ResearchFieldViewSet.as_view({'delete': 'destroy'}), name='delete-research-field'),

    #Research Establishment
    path('researchEstablishment/', views.ResearchEstablishmentViewSet.as_view({'get':'list'}), name='list-research-establishment'),
    path('researchEstablishment/create/', views.ResearchEstablishmentViewSet.as_view({'post':'create'}), name='create-research-establishment'),
    path('researchEstablishment/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'get':'retrieve'}), name='retrieve-research-establishment'),
    path('researchEstablishment/update/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'put': 'update'}), name='update-research-establishment'),
    path('researchEstablishment/delete/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'delete': 'destroy'}), name='delete-research-establishment'),
]