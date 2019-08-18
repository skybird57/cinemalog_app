from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
#classes
from cinemalog.Api.rest.serializers import PlanSerializer,UserPlanSerializer
from cinemalog.models import Plan,UserPlan
from users.Api.Rest.checkUserToken import checkUserToken
class PlanList(APIView):    # get all plans
    def get(self,request,format=None):
        userId=request.headers.get('userId') #get parameters
        token=request.headers.get('token')
        if not checkUserToken(userId,token):   #check permission
            raise Exception("userid or token is invalid")
        instance_plan=Plan.objects.all()   #get list of plans
        instance_plan_serializer=PlanSerializer(instance_plan,many=True)  #serialize list
        return Response(instance_plan_serializer.data,status=status.HTTP_200_OK)  #return list

class UserPlanDetail(APIView):  
    def get(self,request,format=None):    # get latest expire date(if we have two expite date give the latest one)
        userId=request.headers.get('userId')   #get parameters
        token=request.headers.get('token')
        if not checkUserToken(userId,token):  #check permissions
            raise Exception("userid or token is invalid")
        instance=expireDate(userId)    #get latest expire date is available
        if instance:
            instance_serializer=UserPlanSerializer(instance)  # serialize latest plan
            return Response(instance_serializer.data,status=status.HTTP_200_OK) #return latest plan
        else:
            return Response("Expire Pleae buy new plan")   #if coudn't find any plan
    def post(self,request,format=None):   #buy new plan
        userId=request.headers.get('userId')  # get parameters
        token=request.headers.get('token')
        planId=request.headers.get('planId')
        if not checkUserToken(userId,token):   #check permission
            raise Exception("userid or token is invalid")
        instance_userplan=UserPlan.objects.filter(user_id=userId).exclude(status=1) #get records which status!=expire
        if 0<len(instance_userplan)<2:  #if user has 1 active plan
            if planId is not None:
                instance_plan=Plan.objects.get(id=planId)  #get selected plan
                latest_userplan=expireDate(userId)  #get latest user plan
                new_row=createNewUserPlan(userId,planId,instance_plan.days,latest_userplan.expire_at)# create new plan
                instance_serializer=UserPlanSerializer(new_row)  #serialize new plan
                return Response(instance_serializer.data,status=status.HTTP_201_CREATED) #return new plan
        elif len(instance_userplan)==0:  #if user dosen't have any plan
            instance_plan=Plan.objects.get(id=planId) # get selected plan
            new_row=createNewUserPlan(userId,planId,instance_plan.days,datetime.today()) # create new plan
            instance_serializer=UserPlanSerializer(new_row) #serialize new plan
            return Response(instance_serializer.data,status=status.HTTP_201_CREATED) #return new plan
        else:    
            return Response("you have two active plan",status=status.HTTP_400_BAD_REQUEST) #we couldn't add more than 2 plan

from django.utils.timezone import now,timedelta
def expireDate(userId):  #get latest avtive plan of user if available 
    try:
        instance=UserPlan.objects.filter(user_id=userId).exclude(status=1).order_by('-expire_at').first() # get last active expire date 
        print('instanceeeeeeeeee:   ',instance)
        d=now()-timedelta(seconds=5)  # get now
        if d<=instance.expire_at: # compare expire date and now
            return instance   # not expire
        else:
            return None  # expire
    except Exception:
         return None  #there is no data means expire

def createNewUserPlan(userId,planId,days,lastExpiredate):  # create new user plan
    instance=UserPlan()
    instance.user_id=userId
    instance.plan_id=planId
    instance.buy_at=datetime.today()
    instance.expire_at=lastExpiredate+timedelta(days=days)
    instance.status=0
    instance.save()
    return instance
