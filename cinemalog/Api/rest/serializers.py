from rest_framework import serializers
from cinemalog.models import ApplicationVersion,Video,Question,News

class VideoSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True,source='user.username')
    class Meta:
        model=Video
        fields='__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    #status=serializers.IntegerField()
    #message=serializers.CharField()
    #link=serializers.CharField()
    class Meta:
        model=ApplicationVersion
        fields='__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'