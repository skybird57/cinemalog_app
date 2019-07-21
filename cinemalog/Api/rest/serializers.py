from rest_framework import serializers
from cinemalog.models import ApplicationVersion
from rest_framework.decorators import APIView
from rest_framework.response import Response
class ApplicationSerializer(serializers.ModelSerializer):
    #status=serializers.IntegerField()
    #message=serializers.CharField()
    #link=serializers.CharField()
    class Meta:
        model=ApplicationVersion
        fields='__all__'


class ForceUpdate(APIView):
    ss=0
    def get(self,request,format=None):
        version=request.query_params.get('version')
        platform=request.query_params.get('platform')
        try:
            instance=ApplicationVersion.objects.filter(platform=platform).order_by('-last_version').first()
        except ApplicationVersion.DoesNotExist:
            return None
        serializer_instance=ApplicationSerializer(instance)
        #return Response(serializer_instance.data['required_version'])
        if float(version)<serializer_instance.data['required_version']:
            ss=1

        return Response(ss)