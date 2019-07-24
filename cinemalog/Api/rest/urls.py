from django.conf.urls import url
from django.urls import path,include
from cinemalog.Api.rest import forceupdate,dialog,question,news


urlpatterns=[
    path('forceupdate',forceupdate.ForceUpdate.as_view(),name="rest force update"),
    path('dialog',dialog.VideoList.as_view(),name="dialog list"),
    url(r'^dialog/(?P<id>[0-9]+)$',dialog.VideoDetail.as_view(),name='detail dialog'),
    path('question',question.QuestionList.as_view(),name="question list"),
    url(r'^question/(?P<id>[0-9]+)$',question.QuestionDeatail.as_view(),name='detail question'),
    path('news',news.NewsList.as_view(),name="news list"),
    url(r'^news/(?P<id>[0-9]+)$',news.NewsDetail.as_view(),name='detail news'),
]
