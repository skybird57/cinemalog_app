from django.conf.urls import url
from django.urls import path,include
from cinemalog.Api.rest import forceupdate,dialog,competition,question,answer,news


urlpatterns=[
    path('forceupdate',forceupdate.ForceUpdate.as_view(),name="rest force update"),
    path('dialog',dialog.VideoList.as_view(),name="dialog list"),
    url(r'^dialog/(?P<id>[0-9]+)$',dialog.VideoDetail.as_view(),name='detail dialog'),
    path('competition',competition.CompetitionList.as_view(),name="competition list"),
    url(r'^competition/(?P<id>[0-9]+)$',competition.CompetitionDetail.as_view(),name='detail competition'),
    path('question',question.QuestionList.as_view(),name="question list"),
    url(r'^question/(?P<id>[0-9]+)$',question.QuestionDeatail.as_view(),name='detail question'),
    path('answer',answer.RegisterAnswer.as_view(),name="answer register"),
    path('news',news.NewsList.as_view(),name="news list"),
    url(r'^news/(?P<id>[0-9]+)$',news.NewsDetail.as_view(),name='detail news'),
]
