from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from datetime import datetime
from cinemalog.AdminApi.Rest.serializers import VideoSerializer,QuestionSerializer,CompetitionSerializer
from cinemalog.models import Question,Competition,Video
from cinemalog.AdminApi.Rest.permissions import IsOwnerOrReadOnly

class QuestionViewSet(viewsets.ModelViewSet):
    
    """
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list` and `detail` actions.
    
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    
    """
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

    
class CompetitionViewSet(viewsets.ModelViewSet):
    
    """
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list` and `detail` actions.
    
    viewsets.ReadOnlyModelViewSet
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    
    """
    queryset=Competition.objects.all()
    serializer_class=CompetitionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #print('srializerrrrrrrrrrrrrrrr',serializer.data)
        #competition=Competition(title=serializer.data['title'],created_at=datetime.today(),user=request.user)
        #serializer.data['user']=request.user
        #serializer.data['created_at']=datetime.today()
        serializer.save(created_at=datetime.today(),user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class VideoViewSet(viewsets.ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer