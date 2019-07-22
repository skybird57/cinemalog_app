from django.conf.urls import url
from django.urls import path,include
from cinemalog.Api.rest import forceupdate,dialoglist,questionlist
urlpatterns=[
    path('forceupdate',forceupdate.ForceUpdate.as_view(),name="rest force update"),
    path('dialoglist',dialoglist.VideoList.as_view(),name="dialog list"),
    path('questionlist',questionlist.QuestionList.as_view(),name="question list"),
]