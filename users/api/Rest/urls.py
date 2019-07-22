from django.urls import path
from django.conf.urls import url,include
from users.Api.Rest import signup


urlpatterns=[
    path('signup',signup.SignUp.as_view(),name='sign up'),
]