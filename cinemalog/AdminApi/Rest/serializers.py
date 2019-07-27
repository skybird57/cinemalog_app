from rest_framework import serializers
from cinemalog.models import Video,ApplicationVersion,SendPush,Question,Competition

class VideoSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True, source='user.username')
    class Meta:
        model=Video
        fields='__all__'
        #fields=('film_name',)

class SendpushSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True,source='user.username')
    class Meta:
        model=SendPush
        fields='__all__'

class ApplicationVersionSerializer(serializers.ModelSerializer):
    #becuase we put manualy the user_id
    #user=serializers.CharField(read_only=True,source='user.usermane')
    class Meta:
        model=ApplicationVersion
        fields='__all__'

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    user=serializers.CharField(read_only=True,source='user.username')
    class Meta:
        model=Question
        fields='__all__'

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    user=serializers.CharField(read_only=True,source='user.username')
    class Meta:
        model=Competition
        fields=('title','release','release_date','updated_at','deleted_at','user')