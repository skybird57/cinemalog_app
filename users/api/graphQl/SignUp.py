import graphene
from users.models import CustomUser,CustomUserToken
from users.Api.GraphQl.types import UserType,TokenType
import re # regex check mobile format

class SignupInput(graphene.InputObjectType): # inputs from mobile
    phone=graphene.String()
    deviceId=graphene.String()
    deviceType=graphene.Int()
    validToken=graphene.String()
class Signup(graphene.Mutation):
    userSignUp=graphene.Field(TokenType)
    class Arguments:
        input=SignupInput()

    def mutate(self,info,input): # mutation_signup 
        p=re.search('^09[0-3]{1}[0-9]{8}$',input['phone'])  # phone format
        if not p:
            raise Exception("phone format is wrong") # phon format wrong
        d=re.search('^(0|1)$',str(input['deviceType']))
        if not d:
            raise Exception("device type is wrong") # device type  wrong
        try:
            user_instance= CustomUser.objects.get(phone=input['phone']) # get user
            id=user_instance.id   # get id
            try:
                token_instance=CustomUserToken.objects.get(user_id=id,deviceId=input['deviceId']) # get token
                token_instance.token=uuid.uuid4().hex   # update token
                token_instance.save()
                return Signup(userSignUp=token_instance)  # return token
            except CustomUserToken.DoesNotExist:
                token_instance=createtoken(id,input)   # create token if is invalid
                return Signup(userSignUp=token_instance)  #return token

        except CustomUser.DoesNotExist:
            raise Exception("user is not valid") # is user not found

class Mutation(graphene.ObjectType):
    signup=Signup.Field()

# create new token
import uuid
def createtoken(id,input):
    try:
        token=CustomUserToken()
        token.token=uuid.uuid4().hex
        token.user_id=id
        token.deviceId=input['deviceId']
        token.deviceType=input['deviceType']
        token.validToken=input['validToken']
        token.save()
        return token    
    except Exception:
        return None