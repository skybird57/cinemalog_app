from rest_framework import serializers
from users.models import CustomUser,CustomUserToken
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('id','username','phone',)

class UserTokenSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True,source='user.phone')
    class Meta:
        model=CustomUserToken
        fields='__all__'
