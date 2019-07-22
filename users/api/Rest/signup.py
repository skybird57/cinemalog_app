from rest_framework.decorators import APIView #model api
from rest_framework.response import Response # return method
from rest_framework import status # response status url
from users.models import User,UserToken #models
from users.Api.Rest.serializers import UserSerializer,UserTokenSerializer # serializers

class SignUp(APIView):
    # get method
    def get(self,request,format=None):
        phone=request.query_params.get('phone') # get phone from request
        try:
            user_instance=User.objects.get(phone=phone) # get user
        except User.DoesNotExist:
            user_instance=createuser(phone)    # create user if not exist
        serializer_userinstance=UserSerializer(user_instance)  # serialize user
        if serializer_userinstance:
            id=serializer_userinstance.data['id'] # get user id
            try:
                token_instance=UserToken.objects.get(user_id=id)  # find user token
            except UserToken.DoesNotExist:
                token_instance=createtoken(id)

            serializer_tokeninstance=UserTokenSerializer(token_instance)  # serialize token
            if token_instance:
                return Response(serializer_tokeninstance.data['token'],status=status.HTTP_200_OK) #return token

# create new user    
def createuser(phone):
        user=User()
        user.phone=phone
        user.save()
        if createtoken(user.id):
            return user
# create new token
def createtoken(id):
    token=UserToken()
    token.token="gfagaergarggag"
    token.user_id=id
    token.save()
    return token    
'''
from users.Api.Rest.serializers import AuthTokenSerializer
from rest_auth.models import TokenModel
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username':user.username})'''