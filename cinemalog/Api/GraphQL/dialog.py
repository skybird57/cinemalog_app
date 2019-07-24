import graphene
#classes and functions
from cinemalog.Api.GraphQL.types import VideoType
from cinemalog.models import Video,VideoView
from users.Api.Rest.checkUserToken import checkUserToken  # to check token

class Query(graphene.ObjectType):
    videos=graphene.List(VideoType,  #args
                userId=graphene.Int(),  #kwargs
                token=graphene.String()) #kwargs
    video_detail=graphene.Field(VideoType,
                id=graphene.Int(),#kwargs
                userId=graphene.Int(),#kwargs
                token=graphene.String())#kwargs

    def resolve_videos(self,info,userId,token):
        if not checkUserToken(userId,token):   # check user token
            raise Exception("Your user_id or token is invalid")   
        instance=Video.objects.all()  # get all videos
        return instance   # return all videos

    def resolve_video_detail(self,info,**kwargs):
        try:
            id=kwargs.get('id')   # get parameters from kwargs
            userId=kwargs.get('userId')
            token=kwargs.get('token')
        except Exception:
            raise Exception("Your parameters are wrong")

        if not checkUserToken(userId,token):   #check user token
            raise Exception("Your user_id or token is invalid")
        if id is not None:  # chech id
            try:
                instance=Video.objects.get(pk=id) # get record
                if videoViewIncreament(userId,instance.id):  #check is user view this video befor or not
                    instance.view+=1   # add number og view
                    instance.save()  # save updated record
                    instance.message="Increament Done"
                instance.message="ok"  # set message
            except Video.DoesNotExist:
                raise Exception("Video ID is invalid")
        return instance  # return video

from datetime import datetime  # use for viewAt field
def videoViewIncreament(userId,videoId):
    if userId and videoId is not None:  # check parameters
        try:
            videoView=VideoView.objects.get(user_id=userId,video_id=videoId) # if seen befor return false
            return False
        except Exception:
            videoView=VideoView(user_id=userId,video_id=videoId,viewAt=datetime.today())
            videoView.save()  #if not seen before create new record and register user and video and return true
            return True

'''
# increament video views
class VideoViewIncreament(graphene.Mutation):
    video=graphene.Field(VideoType)
                
    class Arguments:
        id=graphene.Int()
        userId=graphene.Int()
        token=graphene.String()

    def mutate(self,info,id,userId,token):
        if not checkUserToken(userId,token):   #check user token
            raise Exception("Your user_id or token is invalid")
        if id is not None:  # chech id
            try:
                instance=Video.objects.get(pk=id) # get record
                instance.view+=1
                instance.save()
                instance.message="increament Done"
                return VideoViewIncreament(video=instance)
            except Video.DoesNotExist:
                raise Exception("ID is invalid")
            

class Mutation(graphene.ObjectType):
    videoViewIncreament=VideoViewIncreament.Field()
'''