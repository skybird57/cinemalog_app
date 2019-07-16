"""Cinemalogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.utils.translation import ugettext

#change ‘Django administration’ text
admin.site.site_header = ugettext("Cinema-log Admin")
admin.site.site_title = ugettext("Cinema-log Admin Portal")
admin.site.index_title = ugettext("Welcome to Cinema-log Researcher Portal")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cinemalog/',include('cinemalog.urls')),
    path('user/',include('users.urls')),
]
