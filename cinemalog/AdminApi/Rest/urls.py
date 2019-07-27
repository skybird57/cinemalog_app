from django.urls import path,include
from django.conf.urls import url
from cinemalog.AdminApi.Rest import json_api_view as jviews
from cinemalog.AdminApi.Rest import api_api_view as aviews
from cinemalog.AdminApi.Rest import api_view as avviews
from cinemalog.AdminApi.Rest import mixin_api,generic_api
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
]

#baraye login shodan dar rest api
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns+=[path('api-auth/', include('rest_framework.urls')),]
urlpatterns=format_suffix_patterns(urlpatterns)

# baraye rest-auth va gereftane token
urlpatterns+=[url(r'^rest-auth/', include('rest_auth.urls'))]

# using router for viewset
from rest_framework.routers import DefaultRouter
from cinemalog.AdminApi.Rest import viewset_api 
from users.AdminApi.Rest import viewsetUser
router=DefaultRouter()
router.register(r'questions',viewset_api.QuestionViewSet)
router.register(r'competitions',viewset_api.CompetitionViewSet)
router.register(r'Video',viewset_api.VideoViewSet)
router.register(r'User',viewsetUser.AdminUserViewSet)
urlpatterns+=[path('',include(router.urls)),]

