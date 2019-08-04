from django.urls import path
from django.conf.urls import url,include
from users.Api.Rest import getphone,signup,updateprofile,logout


urlpatterns=[
    path('getphone',getphone.getphone.as_view(),name='get phone'),
    path('signup',signup.SignUp.as_view(),name='sign up'),
    path('updateprofile',updateprofile.UpdateProfile.as_view(),name='update profile'),
    path('logout',logout.Logout.as_view(),name='log out'),
]