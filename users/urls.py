from django.urls import path
from django.conf.urls import url,include
from users import views

urlpatterns=[
    path('index',views.index,name='user index'),
    path('api/',include('users.Api.Rest.urls')),
]
