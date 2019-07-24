import graphene
#classes and functions
from cinemalog.Api.GraphQL.types import NewsType
from cinemalog.models import News,NewsView
from users.Api.Rest.checkUserToken import checkUserToken  # to check token

class Query(graphene.ObjectType):
    news=graphene.List(NewsType,  #args
                userId=graphene.Int(),  #kwargs
                token=graphene.String()) #kwargs
    news_detail=graphene.Field(NewsType,
                id=graphene.Int(),#kwargs
                userId=graphene.Int(),#kwargs
                token=graphene.String())#kwargs

    def resolve_news(self,info,userId,token):
        if not checkUserToken(userId,token):   # check user token
            raise Exception("Your user_id or token is invalid")   
        instance=News.objects.all()  # get all videos
        return instance   # return all news

    def resolve_news_detail(self,info,**kwargs):
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
                instance=News.objects.get(pk=id) # get record
                if newsViewIncreament(userId,instance.id):  #check is user view this news befor or not
                    instance.view+=1   # add number og view
                    instance.save()  # save updated record
                    instance.message="Increament Done"
                instance.message="ok"  # set message
            except News.DoesNotExist:
                raise Exception("News ID is invalid")
        return instance  # return news

from datetime import datetime  # use for viewAt field
def newsViewIncreament(userId,newsId):
    if userId and newsId is not None:  # check parameters
        try:
            newsView=NewsView.objects.get(user_id=userId,news_id=newsId) # if seen befor return false
            return False
        except Exception:
            newsView=NewsView(user_id=userId,news_id=newsId,viewAt=datetime.today())
            newsView.save()  #if not seen before create new record and register user and video and return true
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