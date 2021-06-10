from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from database import views

urlpatterns = [
    # path('', include(router.urls)),
    path('search/', views.Search, name='search'),

    #Modify ressources
    path('modify/', views.ModifyRessource.as_view(), name='modify'),

    #Date endpoint
    path('dates/', views.DateViewSet.as_view({'get': 'list'}), name='list-dates'),
    path('date/create/', views.DateViewSet.as_view({'post': 'create'}), name='create-date'),
    path('date/<int:pk>/', views.DateViewSet.as_view({'get': 'retrieve'}), name='retrieve-date'),
    path('date/update/<int:pk>/', views.DateViewSet.as_view({'put': 'update'}), name='update-date'),
    path('date/delete/<int:pk>/', views.DateViewSet.as_view({'delete': 'destroy'}), name='delete-date'),

    #Quality endpoint
    path('qualities/', views.QualityViewSet.as_view({'get': 'list'}), name='list-qualities'),
    path('quality/create/', views.QualityViewSet.as_view({'post': 'create'}), name='create-quality'),
    path('quality/<int:pk>/', views.QualityViewSet.as_view({'get': 'retrieve'}), name='retrieve-quality'),
    path('quality/update/<int:pk>/', views.QualityViewSet.as_view({'put': 'update'}), name='update-quality'),
    path('quality/delete/<int:pk>/', views.QualityViewSet.as_view({'delete': 'destroy'}), name='delete-quality'),

    #Knowledge endpoint
    path('knowledges/', views.KnowledgeViewSet.as_view({'get': 'list'}), name='list-knowledges'),
    path('knowledge/create/', views.KnowledgeViewSet.as_view({'post': 'create'}), name='create-knowledge'),
    path('knowledge/<int:pk>/', views.KnowledgeViewSet.as_view({'get': 'retrieve'}), name='retrieve-knowledge'),
    path('knowledge/update/<int:pk>/', views.KnowledgeViewSet.as_view({'put': 'update'}), name='update-knowledge'),
    path('knowledge/delete/<int:pk>/', views.KnowledgeViewSet.as_view({'delete': 'destroy'}), name='delete-knowledge'),

    #Collective actor endpoint
    path('collectiveActors/', views.CollectiveActorViewSet.as_view({'get': 'list'}), name='list-collectiveActors'),
    path('collectiveActor/create/', views.CollectiveActorViewSet.as_view({'post': 'create'}), name='create-collectiveActor'),
    path('collectiveActor/<int:pk>/', views.CollectiveActorViewSet.as_view({'get': 'retrieve'}), name='retrieve-collectiveActor'),
    path('collectiveActor/update/<int:pk>/', views.CollectiveActorViewSet.as_view({'put': 'update'}), name='update-collectiveActor'),
    path('collectiveActor/delete/<int:pk>/', views.CollectiveActorViewSet.as_view({'delete': 'destroy'}), name='delete-collectiveActor'),

    #Abstract object endpoint
    path('abstractObjects/', views.AbstractObjectViewSet.as_view({'get': 'list'}), name='list-abstractObjects'),
    path('abstractObject/create/', views.AbstractObjectViewSet.as_view({'post': 'create'}), name='create-abstractObject'),
    path('abstractObject/<int:pk>/', views.AbstractObjectViewSet.as_view({'get': 'retrieve'}), name='retrieve-abstractObject'),
    path('abstractObject/update/<int:pk>/', views.AbstractObjectViewSet.as_view({'put': 'update'}), name='update-abstractObject'),
    path('abstractObject/delete/<int:pk>/', views.AbstractObjectViewSet.as_view({'delete': 'destroy'}), name='delete-abstractObject'),

    #Profession endpoint
    path('professions/', views.ProfessionViewSet.as_view({'get': 'list'}), name='list-professions'),
    path('profession/create/', views.ProfessionViewSet.as_view({'post': 'create'}), name='create-profession'),
    path('profession/<int:pk>/', views.ProfessionViewSet.as_view({'get': 'retrieve'}), name='retrieve-profession'),
    path('profession/update/<int:pk>/', views.ProfessionViewSet.as_view({'put': 'update'}), name='update-profession'),
    path('profession/delete/<int:pk>/', views.ProfessionViewSet.as_view({'delete': 'destroy'}), name='delete-profession'),

    # """
    # Social & associates endpoints
    # """

    #Social activity endpoint
    path('socialActivities/', views.SocialActivityViewSet.as_view({'get': 'list'}), name='list-socialActivities'),
    path('socialActivity/create/', views.SocialActivityViewSet.as_view({'post': 'create'}), name='create-socialActivity'),
    path('socialActivity/<int:pk>/', views.SocialActivityViewSet.as_view({'get': 'retrieve'}), name='retrieve-socialActivity'),
    path('socialActivity/update/<int:pk>/', views.SocialActivityViewSet.as_view({'put': 'update'}), name='update-socialActivity'),
    path('socialActivity/delete/<int:pk>/', views.SocialActivityViewSet.as_view({'delete': 'destroy'}), name='delete-socialActivity'),

    #Social link endpoint
    path('socialLinks/', views.SocialLinkViewSet.as_view({'get': 'list'}), name='list-socialLinks'),
    path('socialLink/create/', views.SocialLinkViewSet.as_view({'post': 'create'}), name='create-socialLink'),
    path('socialLink/<int:pk>/', views.SocialLinkViewSet.as_view({'get': 'retrieve'}), name='retrieve-socialLink'),
    path('socialLink/update/<int:pk>/', views.SocialLinkViewSet.as_view({'put': 'update'}), name='update-socialLink'),
    path('socialLink/delete/<int:pk>/', views.SocialLinkViewSet.as_view({'delete': 'destroy'}), name='delete-socialLink'),

    # """
    # Sources & associates endpoint
    # """

    #Author endpoint
    path('authors/', views.AuthorViewSet.as_view({'get': 'list'}), name='list-authors'),
    path('author/create/', views.AuthorViewSet.as_view({'post': 'create'}), name='create-author'),
    path('author/<int:pk>/', views.AuthorViewSet.as_view({'get': 'retrieve'}), name='retrieve-author'),
    path('author/update/<int:pk>/', views.AuthorViewSet.as_view({'put': 'update'}), name='update-author'),
    path('author/delete/<int:pk>/', views.AuthorViewSet.as_view({'delete': 'destroy'}), name='delete-author'),

    #Content endpoint
    path('contents/', views.ContentViewSet.as_view({'get': 'list'}), name='list-contents'),
    path('content/create/', views.ContentViewSet.as_view({'post': 'create'}), name='create-content'),
    path('content/<int:pk>/', views.ContentViewSet.as_view({'get': 'retrieve'}), name='retrieve-content'),
    path('content/update/<int:pk>/', views.ContentViewSet.as_view({'put': 'update'}), name='update-content'),
    path('content/delete/<int:pk>/', views.ContentViewSet.as_view({'delete': 'destroy'}), name='delete-content'),

    #Ressource endpoint
    path('ressources/', views.RessourceViewSet.as_view({'get': 'list'}), name='list-ressources'),
    path('ressource/create/', views.RessourceViewSet.as_view({'post': 'create'}), name='create-ressource'),
    path('ressource/<int:pk>/', views.RessourceViewSet.as_view({'get': 'retrieve'}), name='retrieve-ressource'),
    path('ressource/update/<int:pk>/', views.RessourceViewSet.as_view({'put': 'update'}), name='update-ressource'),
    path('ressource/delete/<int:pk>/', views.RessourceViewSet.as_view({'delete': 'destroy'}), name='delete-ressource'),


    #Files endpoint
    path('files/', views.FilesViewSet.as_view({'get': 'list'}), name='list-files'),
    path('file/create/', views.FilesViewSet.as_view({'post': 'create'}), name='create-file'),
    path('file/<int:pk>/', views.FilesViewSet.as_view({'get': 'retrieve'}), name='retrieve-file'),
    path('file/update/<int:pk>/', views.FilesViewSet.as_view({'put': 'update'}), name='update-file'),
    path('file/delete/<int:pk>/', views.FilesViewSet.as_view({'delete': 'destroy'}), name='delete-file'),

    #Source endpoint
    path('sources/', views.SourceViewSet.as_view({'get': 'list'}), name='list-sources'),
    path('source/create/', views.SourceViewSet.as_view({'post': 'create'}), name='create-source'),
    path('source/<int:pk>/', views.SourceViewSet.as_view({'get': 'retrieve'}), name='retrieve-source'),
    path('source/update/<int:pk>/', views.SourceViewSet.as_view({'put': 'update'}), name='update-source'),
    path('source/delete/<int:pk>/', views.SourceViewSet.as_view({'delete': 'destroy'}), name='delete-source'),

    # """
    # Place & associate enpoints
    # """

    #Place location endpoint
    path('placeLocations/', views.PlaceLocationViewSet.as_view({'get': 'list'}), name='list-placeLocations'),
    path('placeLocation/create/', views.PlaceLocationViewSet.as_view({'post': 'create'}), name='create-placeLocation'),
    path('placeLocation/<int:pk>/', views.PlaceLocationViewSet.as_view({'get': 'retrieve'}), name='retrieve-placeLocation'),
    path('placeLocation/update/<int:pk>/', views.PlaceLocationViewSet.as_view({'put': 'update'}), name='update-placeLocation'),
    path('placeLocation/delete/<int:pk>/', views.PlaceLocationViewSet.as_view({'delete': 'destroy'}), name='delete-placeLocation'),

    #Place type endpoint
    path('placeTypes/', views.PlaceTypeViewSet.as_view({'get': 'list'}), name='list-placeTypes'),
    path('placeType/create/', views.PlaceTypeViewSet.as_view({'post': 'create'}), name='create-placeType'),
    path('placeType/<int:pk>/', views.PlaceTypeViewSet.as_view({'get': 'retrieve'}), name='retrieve-placeType'),
    path('placeType/update/<int:pk>/', views.PlaceTypeViewSet.as_view({'put': 'update'}), name='update-placeType'),
    path('placeType/delete/<int:pk>/', views.PlaceTypeViewSet.as_view({'delete': 'destroy'}), name='delete-placeType'),

    #Place endpoint
    path('places/', views.PlaceViewSet.as_view({'get': 'list'}), name='list-places'),
    path('place/create/', views.PlaceViewSet.as_view({'post': 'create'}), name='create-place'),
    path('place/<int:pk>/', views.PlaceViewSet.as_view({'get': 'retrieve'}), name='retrieve-place'),
    path('place/update/<int:pk>/', views.PlaceViewSet.as_view({'put': 'update'}), name='update-place'),
    path('place/delete/<int:pk>/', views.PlaceViewSet.as_view({'delete': 'destroy'}), name='delete-place'),

    # """
    # Actor & associate endpoints
    # """

    #Actor endpoint
    path('actors/', views.ActorViewSet.as_view({'get': 'list'}), name='list-actors'),
    path('actor/create/', views.ActorViewSet.as_view({'post': 'create'}), name='create-actor'),
    path('actor/<int:pk>/', views.ActorViewSet.as_view({'get': 'retrieve'}), name='retrieve-actor'),
    path('actor/update/<int:pk>/', views.ActorViewSet.as_view({'put': 'update'}), name='update-actor'),
    path('actor/delete/<int:pk>/', views.ActorViewSet.as_view({'delete': 'destroy'}), name='delete-actor'),

    #Name actor endpoint
    path('nameActors/', views.NameActorViewSet.as_view({'get': 'list'}), name='list-nameActors'),
    path('nameActor/create/', views.NameActorViewSet.as_view({'post': 'create'}), name='create-nameActor'),
    path('nameActor/<int:pk>/', views.NameActorViewSet.as_view({'get': 'retrieve'}), name='retrieve-nameActor'),
    path('nameActor/update/<int:pk>/', views.NameActorViewSet.as_view({'put': 'update'}), name='update-nameActor'),
    path('nameActor/delete/<int:pk>/', views.NameActorViewSet.as_view({'delete': 'destroy'}), name='delete-nameActor'),

    # """
    # Object & associate endpoints
    # """

    #Detail caracteristic endpoint
    path('detailCaracteristics/', views.DetailCaracteristicViewSet.as_view({'get': 'list'}), name='list-detailCaracteristics'),
    path('detailCaracteristic/create/', views.DetailCaracteristicViewSet.as_view({'post': 'create'}), name='create-detailCaracteristic'),
    path('detailCaracteristic/<int:pk>/', views.DetailCaracteristicViewSet.as_view({'get': 'retrieve'}), name='retrieve-detailCaracteristic'),
    path('detailCaracteristic/update/<int:pk>/', views.DetailCaracteristicViewSet.as_view({'put': 'update'}), name='update-detailCaracteristic'),
    path('detailCaracteristic/delete/<int:pk>/', views.DetailCaracteristicViewSet.as_view({'delete': 'destroy'}), name='delete-detailCaracteristic'),

    #Type object endpoint
    path('typeObjects/', views.TypeObjectViewSet.as_view({'get': 'list'}), name='list-typeObjects'),
    path('typeObject/create/', views.TypeObjectViewSet.as_view({'post': 'create'}), name='create-typeObject'),
    path('typeObject/<int:pk>/', views.TypeObjectViewSet.as_view({'get': 'retrieve'}), name='retrieve-typeObject'),
    path('typeObject/update/<int:pk>/', views.TypeObjectViewSet.as_view({'put': 'update'}), name='update-typeObject'),
    path('typeObject/delete/<int:pk>/', views.TypeObjectViewSet.as_view({'delete': 'destroy'}), name='delete-typeObject'),

    #Energy endpoint
    path('energies/', views.EnergyViewSet.as_view({'get': 'list'}), name='list-energies'),
    path('energy/create/', views.EnergyViewSet.as_view({'post': 'create'}), name='create-energy'),
    path('energy/<int:pk>/', views.EnergyViewSet.as_view({'get': 'retrieve'}), name='retrieve-energy'),
    path('energy/update/<int:pk>/', views.EnergyViewSet.as_view({'put': 'update'}), name='update-energy'),
    path('energy/delete/<int:pk>/', views.EnergyViewSet.as_view({'delete': 'destroy'}), name='delete-energy'),

    #Building endpoint
    path('typologies/', views.TypologieViewSet.as_view({'get': 'list'}), name='list-typologies'),
    path('typology/create/', views.TypologieViewSet.as_view({'post': 'create'}), name='create-typology'),
    path('typology/<int:pk>/', views.TypologieViewSet.as_view({'get': 'retrieve'}), name='retrieve-typology'),
    path('typology/update/<int:pk>/', views.TypologieViewSet.as_view({'put': 'update'}), name='update-typology'),
    path('typology/delete/<int:pk>/', views.TypologieViewSet.as_view({'delete': 'destroy'}), name='delete-typology'),

    #Object endpoint
    path('objects/', views.ObjectViewSet.as_view({'get': 'list'}), name='list-objects'),
    path('object/create/', views.ObjectViewSet.as_view({'post': 'create'}), name='create-object'),
    path('object/<int:pk>/', views.ObjectViewSet.as_view({'get': 'retrieve'}), name='retrieve-object'),
    path('object/update/<int:pk>/', views.ObjectViewSet.as_view({'put': 'update'}), name='update-object'),
    path('object/delete/<int:pk>/', views.ObjectViewSet.as_view({'delete': 'destroy'}), name='delete-object'),

    #Caracteristic endpoint
    path('caracteristics/', views.CaracteristicViewSet.as_view({'get': 'list'}), name='list-caracteristics'),
    path('caracteristic/create/', views.CaracteristicViewSet.as_view({'post': 'create'}), name='create-caracteristic'),
    path('caracteristic/<int:pk>/', views.CaracteristicViewSet.as_view({'get': 'retrieve'}), name='retrieve-caracteristic'),
    path('caracteristic/update/<int:pk>/', views.CaracteristicViewSet.as_view({'put': 'update'}), name='update-caracteristic'),
    path('caracteristic/delete/<int:pk>/', views.CaracteristicViewSet.as_view({'delete': 'destroy'}), name='delete-caracteristic'),
    
]