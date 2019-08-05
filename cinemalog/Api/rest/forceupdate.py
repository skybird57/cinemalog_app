from rest_framework.decorators import APIView
from cinemalog.Api.rest.serializers import ApplicationSerializer
from cinemalog.models import ApplicationVersion
from rest_framework.decorators import APIView #view method 
from rest_framework.response import Response  # return format


class ForceUpdate(APIView):
    status=0
    message=""
    link=""
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
            status=1
            message="force update"
            link="https:\\updatelink"
        elif float(version)>= serializer_instance.data['required_version'] and float(version)< serializer_instance.data['last_version'] :
            status=2
            message="it's better to update"
            link="https:\\updatelink"
        elif float(version)>= serializer_instance.data['last_version']:
            status=3
            message="it's ok"
            link=""
        return Response((status,message,link))