from django.urls import path,include
from django.conf.urls import url
from cinemalog.Api.rest import json_api_view as jviews
from cinemalog.Api.rest import api_api_view as aviews
from cinemalog.Api.rest import api_view as avviews
from cinemalog.Api.rest import mixin_api,generic_api
urlpatterns=[
    path('index',jviews.index,name='index rest api'),
    #json api urls
    path('japplication_list',jviews.json_list,name='japplication list'),
    url(r'japplication_detail/(?P<pk>[0-9]+)/$',jviews.json_detail,name='japplication detail'),
    #api api urls
    path('asendpush_list',aviews.api_sendpush_list,name='a_sendpush list'),
    url(r'asendpush_detail/(?P<pk>[0-9]+)/$',aviews.api_sendpush_detail,name='a_sendpush detail'),
    #api_view urls
    path('avsendpush_list',avviews.SendPushList.as_view(),name='av_sendpush list'),
    url(r'avsendpush_detail/(?P<pk>[0-9]+)/$',avviews.SendPush_Detail.as_view(),name='av_sendpush detail'),
    #api_mixins urls
    path('mvideo_list',mixin_api.Video_list.as_view(),name='m_video list'),
    url(r'mvideo_detail/(?P<pk>[0-9]+)/$',mixin_api.Video_detail.as_view(),name='m_video detail'),
    #api_generics urls
    path('gvideo_list',generic_api.Video_list.as_view(),name='g_video list'),
    url(r'gvideo_detail/(?P<pk>[0-9]+)/$',generic_api.Video_detail.as_view(),name='g_video detail'),

    # url of roots in apis               you can use one of the root or router
    #url(r'^$',aviews.api_api_root,name='api root1'),
    #url(r'^$',avviews.Api_Root.as_view(),name='api root2'),

    path('mvideo_detail/<int:pk>/highlight/', mixin_api.VideoHighlight.as_view()),
]

# using router for viewset
from rest_framework.routers import DefaultRouter
from cinemalog.Api.rest import viewset_api 
router=DefaultRouter()
router.register(r'questions',viewset_api.QuestionViewSet)
router.register(r'competitions',viewset_api.CompetitionViewSet)

urlpatterns+=[path('',include(router.urls)),]
