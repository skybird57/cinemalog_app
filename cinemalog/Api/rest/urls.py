from django.conf.urls import url
from django.urls import path,include
from cinemalog.Api.rest import serializers
urlpatterns=[
    path('forceupdate',serializers.ForceUpdate.as_view(),name="rest force update"),
]