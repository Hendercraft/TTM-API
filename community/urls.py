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
    path('create/', views.CreateProfile.as_view(), name='create-user-profile'),
    path('<int:pk>/', views.ProfileView.as_view(), name='retrieve-user-profile'),
    path('update/<int:pk>/', views.ProfileView.as_view(), name='update-user-profile'),
    path('delete/<int:pk>/', views.ProfileView.as_view(), name='delete-user-profile'),

    #Testimony
    path('temoignages/', views.TestimonyViewSet.as_view({'get':'list'}), name='list-testimony'),
    path('temoignages/create/', views.TestimonyViewSet.as_view({'post':'create'}), name='create-testimony'),
    path('temoignages/<int:pk>/', views.TestimonyViewSet.as_view({'get':'retrieve'}), name='retrieve-testimony'),
    path('temoignages/update/<int:pk>/', views.TestimonyViewSet.as_view({'put': 'update'}), name='update-testimony'),
    path('temoignages/delete/<int:pk>/', views.TestimonyViewSet.as_view({'delete': 'destroy'}), name='delete-testimony'),

    #Discipline
    path('disciplines/', views.DisciplineViewSet.as_view({'get':'list'}), name='list-discipline'),
    path('discipline/create/', views.DisciplineViewSet.as_view({'post':'create'}), name='create-discipline'),
    path('discipline/<int:pk>/', views.DisciplineViewSet.as_view({'get':'retrieve'}), name='retrieve-discipline'),
    path('discipline/update/<int:pk>/', views.DisciplineViewSet.as_view({'put': 'update'}), name='update-discipline'),
    path('discipline/delete/<int:pk>/', views.DisciplineViewSet.as_view({'delete': 'destroy'}), name='delete-discipline'),

    #Research Fields
    path('champsRecherches/', views.ResearchFieldViewSet.as_view({'get':'list'}), name='list-research-field'),
    path('champRecherche/create/', views.ResearchFieldViewSet.as_view({'post':'create'}), name='create-research-field'),
    path('champRecherche/<int:pk>/', views.ResearchFieldViewSet.as_view({'get':'retrieve'}), name='retrieve-research-field'),
    path('champRecherche/update/<int:pk>/', views.ResearchFieldViewSet.as_view({'put': 'update'}), name='update-research-field'),
    path('champRecherche/delete/<int:pk>/', views.ResearchFieldViewSet.as_view({'delete': 'destroy'}), name='delete-research-field'),

    #Research Establishment
    path('etablisementsRecherches/', views.ResearchEstablishmentViewSet.as_view({'get':'list'}), name='list-research-establishment'),
    path('etablisementRecherche/create/', views.ResearchEstablishmentViewSet.as_view({'post':'create'}), name='create-research-establishment'),
    path('etablisementRecherche/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'get':'retrieve'}), name='retrieve-research-establishment'),
    path('etablisementRecherche/update/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'put': 'update'}), name='update-research-establishment'),
    path('etablisementRecherche/delete/<int:pk>/', views.ResearchEstablishmentViewSet.as_view({'delete': 'destroy'}), name='delete-research-establishment'),


    #Contact message
    path('contacts/', views.ContactViewSet.as_view({'get':'list'}), name='list-contact'),
    path('contact/create/', views.ContactViewSet.as_view({'post':'create'}), name='create-contact'),
    path('contact/<int:pk>/', views.ContactViewSet.as_view({'get':'retrieve'}), name='retrieve-contact'),
    path('contact/update/<int:pk>/', views.ContactViewSet.as_view({'put': 'update'}), name='update-contact'),
    path('contact/delete/<int:pk>/', views.ContactViewSet.as_view({'delete': 'destroy'}), name='delete-contact'),
]