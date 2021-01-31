from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from database import views


# router = routers.DefaultRouter()

# router.register('dates', views.DateViewSet)
# router.register('qualities', views.QualityViewSet)
# router.register('sourceType', views.SourceTypeViewSet)
# router.register('authors', views.AuthorViewSet)
# router.register('contents', views.ContentViewSet)
# router.register('urls', views.UrlViewSet)
# router.register('sources', views.SourceViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('search/', views.Search, name='search'),

    #Date endpoint
    path('date/', views.DateViewSet.as_view({'get': 'list'}), name='list-date'),
    path('date/create/', views.DateViewSet.as_view({'post': 'create'}), name='create-date'),
    path('date/<int:pk>/', views.DateViewSet.as_view({'get': 'retrieve'}), name='retrieve-date'),
    path('date/update/<int:pk>/', views.DateViewSet.as_view({'put': 'update'}), name='update-date'),
    path('date/delete/<int:pk>/', views.DateViewSet.as_view({'delete': 'destroy'}), name='delete-date'),

    #Quality endpoint
    path('quality/', views.QualityViewSet.as_view({'get': 'list'}), name='list-quality'),
    path('quality/create/', views.QualityViewSet.as_view({'post': 'create'}), name='create-quality'),
    path('quality/<int:pk>/', views.QualityViewSet.as_view({'get': 'retrieve'}), name='retrieve-quality'),
    path('quality/update/<int:pk>/', views.QualityViewSet.as_view({'put': 'update'}), name='update-quality'),
    path('quality/delete/<int:pk>/', views.QualityViewSet.as_view({'delete': 'destroy'}), name='delete-quality'),

    #Knowledge endpoint
    path('knowledge/', views.KnowledgeViewSet.as_view({'get': 'list'}), name='list-knowledge'),
    path('knowledge/create/', views.KnowledgeViewSet.as_view({'post': 'create'}), name='create-knowledge'),
    path('knowledge/<int:pk>/', views.KnowledgeViewSet.as_view({'get': 'retrieve'}), name='retrieve-knowledge'),
    path('knowledge/update/<int:pk>/', views.KnowledgeViewSet.as_view({'put': 'update'}), name='update-knowledge'),
    path('knowledge/delete/<int:pk>/', views.KnowledgeViewSet.as_view({'delete': 'destroy'}), name='delete-knowledge'),

    #Collective actor endpoint
    path('collectiveActor/', views.CollectiveActorViewSet.as_view({'get': 'list'}), name='list-collectiveActor'),
    path('collectiveActor/create/', views.CollectiveActorViewSet.as_view({'post': 'create'}), name='create-collectiveActor'),
    path('collectiveActor/<int:pk>/', views.CollectiveActorViewSet.as_view({'get': 'retrieve'}), name='retrieve-collectiveActor'),
    path('collectiveActor/update/<int:pk>/', views.CollectiveActorViewSet.as_view({'put': 'update'}), name='update-collectiveActor'),
    path('collectiveActor/delete/<int:pk>/', views.CollectiveActorViewSet.as_view({'delete': 'destroy'}), name='delete-collectiveActor'),

    #Abstract object endpoint
    path('abstractObject/', views.AbstractObjectViewSet.as_view({'get': 'list'}), name='list-abstractObject'),
    path('abstractObject/create/', views.AbstractObjectViewSet.as_view({'post': 'create'}), name='create-abstractObject'),
    path('abstractObject/<int:pk>/', views.AbstractObjectViewSet.as_view({'get': 'retrieve'}), name='retrieve-abstractObject'),
    path('abstractObject/update/<int:pk>/', views.AbstractObjectViewSet.as_view({'put': 'update'}), name='update-abstractObject'),
    path('abstractObject/delete/<int:pk>/', views.AbstractObjectViewSet.as_view({'delete': 'destroy'}), name='delete-abstractObject'),

    #Profession endpoint
    path('profession/', views.ProfessionViewSet.as_view({'get': 'list'}), name='list-profession'),
    path('profession/create/', views.ProfessionViewSet.as_view({'post': 'create'}), name='create-profession'),
    path('profession/<int:pk>/', views.ProfessionViewSet.as_view({'get': 'retrieve'}), name='retrieve-profession'),
    path('profession/update/<int:pk>/', views.ProfessionViewSet.as_view({'put': 'update'}), name='update-profession'),
    path('profession/delete/<int:pk>/', views.ProfessionViewSet.as_view({'delete': 'destroy'}), name='delete-profession'),

    # """
    # Social & associates endpoints
    # """

    #Social activity endpoint
    path('socialActivity/', views.SocialActivityViewSet.as_view({'get': 'list'}), name='list-socialActivity'),
    path('socialActivity/create/', views.SocialActivityViewSet.as_view({'post': 'create'}), name='create-socialActivity'),
    path('socialActivity/<int:pk>/', views.SocialActivityViewSet.as_view({'get': 'retrieve'}), name='retrieve-socialActivity'),
    path('socialActivity/update/<int:pk>/', views.SocialActivityViewSet.as_view({'put': 'update'}), name='update-socialActivity'),
    path('socialActivity/delete/<int:pk>/', views.SocialActivityViewSet.as_view({'delete': 'destroy'}), name='delete-socialActivity'),

    #Social link endpoint
    path('socialLink/', views.SocialLinkViewSet.as_view({'get': 'list'}), name='list-socialLink'),
    path('socialLink/create/', views.SocialLinkViewSet.as_view({'post': 'create'}), name='create-socialLink'),
    path('socialLink/<int:pk>/', views.SocialLinkViewSet.as_view({'get': 'retrieve'}), name='retrieve-socialLink'),
    path('socialLink/update/<int:pk>/', views.SocialLinkViewSet.as_view({'put': 'update'}), name='update-socialLink'),
    path('socialLink/delete/<int:pk>/', views.SocialLinkViewSet.as_view({'delete': 'destroy'}), name='delete-socialLink'),

    # """
    # Sources & associates endpoint
    # """

    #SourceType endpoint
    path('sourceType/', views.SourceTypeViewSet.as_view({'get': 'list'}), name='list-sourceType'),
    path('sourceType/create/', views.SourceTypeViewSet.as_view({'post': 'create'}), name='create-sourceType'),
    path('sourceType/<int:pk>/', views.SourceTypeViewSet.as_view({'get': 'retrieve'}), name='retrieve-sourceType'),
    path('sourceType/update/<int:pk>/', views.SourceTypeViewSet.as_view({'put': 'update'}), name='update-sourceType'),
    path('sourceType/delete/<int:pk>/', views.SourceTypeViewSet.as_view({'delete': 'destroy'}), name='delete-sourceType'),

    #Author endpoint
    path('author/', views.AuthorViewSet.as_view({'get': 'list'}), name='list-author'),
    path('author/create/', views.AuthorViewSet.as_view({'post': 'create'}), name='create-author'),
    path('author/<int:pk>/', views.AuthorViewSet.as_view({'get': 'retrieve'}), name='retrieve-author'),
    path('author/update/<int:pk>/', views.AuthorViewSet.as_view({'put': 'update'}), name='update-author'),
    path('author/delete/<int:pk>/', views.AuthorViewSet.as_view({'delete': 'destroy'}), name='delete-author'),

    #Content endpoint
    path('content/', views.ContentViewSet.as_view({'get': 'list'}), name='list-content'),
    path('content/create/', views.ContentViewSet.as_view({'post': 'create'}), name='create-content'),
    path('content/<int:pk>/', views.ContentViewSet.as_view({'get': 'retrieve'}), name='retrieve-content'),
    path('content/update/<int:pk>/', views.ContentViewSet.as_view({'put': 'update'}), name='update-content'),
    path('content/delete/<int:pk>/', views.ContentViewSet.as_view({'delete': 'destroy'}), name='delete-content'),

    #Url endpoint
    path('url/', views.UrlViewSet.as_view({'get': 'list'}), name='list-url'),
    path('url/create/', views.UrlViewSet.as_view({'post': 'create'}), name='create-url'),
    path('url/<int:pk>/', views.UrlViewSet.as_view({'get': 'retrieve'}), name='retrieve-url'),
    path('url/update/<int:pk>/', views.UrlViewSet.as_view({'put': 'update'}), name='update-url'),
    path('url/delete/<int:pk>/', views.UrlViewSet.as_view({'delete': 'destroy'}), name='delete-url'),

    #Source endpoint
    path('source/', views.SourceViewSet.as_view({'get': 'list'}), name='list-source'),
    path('source/create/', views.SourceViewSet.as_view({'post': 'create'}), name='create-source'),
    path('source/<int:pk>/', views.SourceViewSet.as_view({'get': 'retrieve'}), name='retrieve-source'),
    path('source/update/<int:pk>/', views.SourceViewSet.as_view({'put': 'update'}), name='update-source'),
    path('source/delete/<int:pk>/', views.SourceViewSet.as_view({'delete': 'destroy'}), name='delete-source'),

    # """
    # Place & associate enpoints
    # """

    #Place location endpoint
    path('placeLocation/', views.PlaceLocationViewSet.as_view({'get': 'list'}), name='list-placeLocation'),
    path('placeLocation/create/', views.PlaceLocationViewSet.as_view({'post': 'create'}), name='create-placeLocation'),
    path('placeLocation/<int:pk>/', views.PlaceLocationViewSet.as_view({'get': 'retrieve'}), name='retrieve-placeLocation'),
    path('placeLocation/update/<int:pk>/', views.PlaceLocationViewSet.as_view({'put': 'update'}), name='update-placeLocation'),
    path('placeLocation/delete/<int:pk>/', views.PlaceLocationViewSet.as_view({'delete': 'destroy'}), name='delete-placeLocation'),

    #Place type endpoint
    path('placeType/', views.PlaceTypeViewSet.as_view({'get': 'list'}), name='list-placeType'),
    path('placeType/create/', views.PlaceTypeViewSet.as_view({'post': 'create'}), name='create-placeType'),
    path('placeType/<int:pk>/', views.PlaceTypeViewSet.as_view({'get': 'retrieve'}), name='retrieve-placeType'),
    path('placeType/update/<int:pk>/', views.PlaceTypeViewSet.as_view({'put': 'update'}), name='update-placeType'),
    path('placeType/delete/<int:pk>/', views.PlaceTypeViewSet.as_view({'delete': 'destroy'}), name='delete-placeType'),

    #Place endpoint
    path('place/', views.PlaceViewSet.as_view({'get': 'list'}), name='list-place'),
    path('place/create/', views.PlaceViewSet.as_view({'post': 'create'}), name='create-place'),
    path('place/<int:pk>/', views.PlaceViewSet.as_view({'get': 'retrieve'}), name='retrieve-place'),
    path('place/update/<int:pk>/', views.PlaceViewSet.as_view({'put': 'update'}), name='update-place'),
    path('place/delete/<int:pk>/', views.PlaceViewSet.as_view({'delete': 'destroy'}), name='delete-place'),

    # """
    # Actor & associate endpoints
    # """

    #Actor endpoint
    path('actor/', views.ActorViewSet.as_view({'get': 'list'}), name='list-actor'),
    path('actor/create/', views.ActorViewSet.as_view({'post': 'create'}), name='create-actor'),
    path('actor/<int:pk>/', views.ActorViewSet.as_view({'get': 'retrieve'}), name='retrieve-actor'),
    path('actor/update/<int:pk>/', views.ActorViewSet.as_view({'put': 'update'}), name='update-actor'),
    path('actor/delete/<int:pk>/', views.ActorViewSet.as_view({'delete': 'destroy'}), name='delete-actor'),

    #Name actor endpoint
    path('nameActor/', views.NameActorViewSet.as_view({'get': 'list'}), name='list-nameActor'),
    path('nameActor/create/', views.NameActorViewSet.as_view({'post': 'create'}), name='create-nameActor'),
    path('nameActor/<int:pk>/', views.NameActorViewSet.as_view({'get': 'retrieve'}), name='retrieve-nameActor'),
    path('nameActor/update/<int:pk>/', views.NameActorViewSet.as_view({'put': 'update'}), name='update-nameActor'),
    path('nameActor/delete/<int:pk>/', views.NameActorViewSet.as_view({'delete': 'destroy'}), name='delete-nameActor'),

    # """
    # Object & associate endpoints
    # """

    #Detail caracteristic endpoint
    path('detailCaracteristic/', views.DetailCaracteristicViewSet.as_view({'get': 'list'}), name='list-detailCaracteristic'),
    path('detailCaracteristic/create/', views.DetailCaracteristicViewSet.as_view({'post': 'create'}), name='create-detailCaracteristic'),
    path('detailCaracteristic/<int:pk>/', views.DetailCaracteristicViewSet.as_view({'get': 'retrieve'}), name='retrieve-detailCaracteristic'),
    path('detailCaracteristic/update/<int:pk>/', views.DetailCaracteristicViewSet.as_view({'put': 'update'}), name='update-detailCaracteristic'),
    path('detailCaracteristic/delete/<int:pk>/', views.DetailCaracteristicViewSet.as_view({'delete': 'destroy'}), name='delete-detailCaracteristic'),

    #Type object endpoint
    path('typeObject/', views.TypeObjectViewSet.as_view({'get': 'list'}), name='list-typeObject'),
    path('typeObject/create/', views.TypeObjectViewSet.as_view({'post': 'create'}), name='create-typeObject'),
    path('typeObject/<int:pk>/', views.TypeObjectViewSet.as_view({'get': 'retrieve'}), name='retrieve-typeObject'),
    path('typeObject/update/<int:pk>/', views.TypeObjectViewSet.as_view({'put': 'update'}), name='update-typeObject'),
    path('typeObject/delete/<int:pk>/', views.TypeObjectViewSet.as_view({'delete': 'destroy'}), name='delete-typeObject'),

    #Energy endpoint
    path('energy/', views.EnergyViewSet.as_view({'get': 'list'}), name='list-energy'),
    path('energy/create/', views.EnergyViewSet.as_view({'post': 'create'}), name='create-energy'),
    path('energy/<int:pk>/', views.EnergyViewSet.as_view({'get': 'retrieve'}), name='retrieve-energy'),
    path('energy/update/<int:pk>/', views.EnergyViewSet.as_view({'put': 'update'}), name='update-energy'),
    path('energy/delete/<int:pk>/', views.EnergyViewSet.as_view({'delete': 'destroy'}), name='delete-energy'),

    #Object endpoint
    path('object/', views.ObjectViewSet.as_view({'get': 'list'}), name='list-object'),
    path('object/create/', views.ObjectViewSet.as_view({'post': 'create'}), name='create-object'),
    path('object/<int:pk>/', views.ObjectViewSet.as_view({'get': 'retrieve'}), name='retrieve-object'),
    path('object/update/<int:pk>/', views.ObjectViewSet.as_view({'put': 'update'}), name='update-object'),
    path('object/delete/<int:pk>/', views.ObjectViewSet.as_view({'delete': 'destroy'}), name='delete-object'),

    #Caracteristic endpoint
    path('caracteristic/', views.CaracteristicViewSet.as_view({'get': 'list'}), name='list-caracteristic'),
    path('caracteristic/create/', views.CaracteristicViewSet.as_view({'post': 'create'}), name='create-caracteristic'),
    path('caracteristic/<int:pk>/', views.CaracteristicViewSet.as_view({'get': 'retrieve'}), name='retrieve-caracteristic'),
    path('caracteristic/update/<int:pk>/', views.CaracteristicViewSet.as_view({'put': 'update'}), name='update-caracteristic'),
    path('caracteristic/delete/<int:pk>/', views.CaracteristicViewSet.as_view({'delete': 'destroy'}), name='delete-caracteristic'),
    
]