from django.urls import path
from django.conf.urls import url,include
from users.Api.Rest import signup,updateprofile


urlpatterns=[
    path('signup',signup.SignUp.as_view(),name='sign up'),
    path('updateprofile',updateprofile.UpdateProfile.as_view(),name='update profile'),
]