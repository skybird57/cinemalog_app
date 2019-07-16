from django.urls import path
from django.conf.urls import include
from cinemalog import views
urlpatterns=[
    path('index/',views.index,name='cinemalog index'),
    path('api/',include('cinemalog.Api.urls')),
]