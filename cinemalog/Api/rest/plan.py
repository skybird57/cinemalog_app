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
        userId=request.query_params.get('userId')
        token=request.query_params.get('token')
        if not checkUserToken(userId,token):
            raise Exception("userid or token is invalid")
        instance_plan=Plan.objects.all()
        instance_plan_serializer=PlanSerializer(instance_plan,many=True)
        return Response(instance_plan_serializer.data,status=status.HTTP_200_OK)

class UserPlanDetail(APIView):  
    def get(self,request,format=None):    # get latest expire date(if we have two expite date give the latest one)
        userId=request.query_params.get('userId')
        token=request.query_params.get('token')
        if not checkUserToken(userId,token):
            raise Exception("userid or token is invalid")
        instance=expireDate(userId)    
        if instance:
            instance_serializer=UserPlanSerializer(instance)
            return Response(instance_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("Expire Pleae buy new plan")
    def post(self,request,format=None):
        userId=request.query_params.get('userId')
        token=request.query_params.get('token')
        planId=request.query_params.get('planId')
        if not checkUserToken(userId,token):
            raise Exception("userid or token is invalid")
        instance_userplan=UserPlan.objects.filter(user_id=userId).exclude(status=1)
        if 0<len(instance_userplan)<2:
            if planId is not None:
                instance_plan=Plan.objects.get(id=planId)
                latest_userplan=expireDate(userId)
                new_row=createNewUserPlan(userId,planId,instance_plan.days,latest_userplan.expire_at)
                instance_serializer=UserPlanSerializer(new_row)
                return Response(instance_serializer.data,status=status.HTTP_201_CREATED)
        elif len(instance_userplan)==0:
            instance_plan=Plan.objects.get(id=planId)
            new_row=createNewUserPlan(userId,planId,instance_plan.days,datetime.today())
            instance_serializer=UserPlanSerializer(new_row)
            return Response(instance_serializer.data,status=status.HTTP_201_CREATED)
        else:    
            return Response("you have two active plan",status=status.HTTP_400_BAD_REQUEST)

from django.utils.timezone import now,timedelta
def expireDate(userId):
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

def createNewUserPlan(userId,planId,days,lastExpiredate):
    instance=UserPlan()
    instance.user_id=userId
    instance.plan_id=planId
    instance.buy_at=datetime.today()
    instance.expire_at=lastExpiredate+timedelta(days=days)
    instance.status=0
    instance.save()
    return instance
    
    
    
