from django.urls import path
from users import views

urlpatterns=[
    path('index',views.index,name='user index'),
]
