from rest_framework import serializers
from cinemalog.models import ApplicationVersion,Video,Competition,Question,UserAnswer,News

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

class CompetitionSerializer(serializers.ModelSerializer):
    list_questions=serializers.CharField(read_only=True,source='question.question')
    class Meta:
        model=Competition
        fields=('id','title','created_at','list_questions')

class QuestionSerializer(serializers.ModelSerializer):
    competition=serializers.CharField(read_only=True,source='competition.title') #change id to title
    user=serializers.CharField(read_only=True,source='user.username')# change id to name
    class Meta:
        model=Question
        fields='__all__'

class UserAnswerSerializer():
    class Meta:
        model=UserAnswer
        fields:'__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'