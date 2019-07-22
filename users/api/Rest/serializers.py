from rest_framework import serializers
from users.models import User,UserToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','phone',)

class UserTokenSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True,source='user.phone')
    class Meta:
        model=UserToken
        fields='__all__'

from rest_framework import authentication
from django.utils.translation import gettext as _
class AuthTokenSerializer(serializers.Serializer):
    phone = serializers.CharField(label=_("phone"))
   

    def validate(self, data):
        phone = data.get('phone')

        if phone:
            user = authentication(phone=phone)
        else:
            msg = _('Must include "phone".')
            raise serializers.ValidationError(msg)

        data['user'] = user
        return data