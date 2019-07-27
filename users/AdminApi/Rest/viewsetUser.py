from rest_framework import viewsets
from users.AdminApi.Rest.serializers import AdminUserSerializer
from django.contrib.auth.models import User

class AdminUserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=AdminUserSerializer