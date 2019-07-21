from django.urls import path
from django.conf.urls import include
from cinemalog import views
from graphene_django.views import GraphQLView  #use for graphql urls
from django.views.decorators.csrf import csrf_exempt # that you need to disable the Django CSRF protection.
from Cinemalogs.schema import schema

#from graphene_file_upload.django import FileUploadGraphQLView
'''
from graphene_django.views import GraphQLView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view


class DRFAuthenticatedGraphQLView(GraphQLView):
    # custom view for using DRF TokenAuthentication with graphene GraphQL.as_view()
    # all requests to Graphql endpoint will require token for auth, obtained from DRF endpoint
    # https://github.com/graphql-python/graphene/issues/249
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(DRFAuthenticatedGraphQLView, cls).as_view(*args, **kwargs)
        view = permission_classes((IsAuthenticatedOrReadOnly,))(view)
        #view = authentication_classes((TokenAuthentication,))(view)
        view = api_view(['POST'])(view)
        return view
'''




urlpatterns=[
    path('index/',views.index,name='cinemalog index'),
    path('api/',include('cinemalog.Api.rest.urls')),
    path('graphql/',csrf_exempt(GraphQLView.as_view(
        graphiql=True,
        schema=schema))),
]


