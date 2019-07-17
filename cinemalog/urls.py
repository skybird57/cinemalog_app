from django.urls import path
from django.conf.urls import include
from cinemalog import views
from graphene_django.views import GraphQLView  #use for graphql urls
from Cinemalogs.schema import schema
urlpatterns=[
    path('index/',views.index,name='cinemalog index'),
    path('api/',include('cinemalog.Api.rest.urls')),
    path('graphql/',GraphQLView.as_view(graphiql=True,schema=schema))
]