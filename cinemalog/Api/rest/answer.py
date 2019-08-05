from rest_framework.decorators import APIView
from rest_framework.response import Response
#classes and Functions
from cinemalog.models import UserAnswer,Question
from cinemalog.Api.rest.serializers import UserAnswerSerializer
from users.models import CustomUser
from users.Api.Rest.checkUserToken import checkUserToken
class RegisterAnswer(APIView):
    
    def post(self,request,format=None):  # get answers jason
        #try:
            userScore=0 # define local score
            userId=request.query_params.get('userId')
            token=request.query_params.get('token')
            if not checkUserToken(userId,token):  # check permission
                raise Exception("user id or token is invalid")  
            data=request.data['answers']    #split json
            #print(data['answers'])
            for item in data:
                comptId=item['cycle_question_id']
                try:
                    userAnswer=UserAnswer.objects.filter(competition_id=comptId,user_id=userId)
                         # check if save before or not 
                        # yani faghat yekbar mitavanad javab dahad
                    print('useridddddd',userAnswer[0].user_id)
                    break     # if save before exit compelatly of for
                except IndexError:
                    for x in item['data']:
                        questionId=x['question']
                        answerId=x['answer']
                        try:  #check is compId and questionId are related
                            question=Question.objects.get(pk=questionId,competition_id=comptId)
                        except Exception:
                            raise Exception("competition info is not matched with question info")
                        try:    # try to add record
                            userAnswer=UserAnswer(competition_id=comptId, # if is not save before add
                                    question_id=questionId,
                                    answer=answerId,
                                    user_id=userId)
                            userAnswer.save()  # save
                            userScore=calculateScore(userId,questionId,answerId) # calculate user score
                        except Exception:
                            raise Exception("couldnt import,wrong information")
            return Response(userScore)  # return user score


def calculateScore(userId,questionId,answerId):  # calculate user score
        question=Question.objects.get(pk=questionId) # get question scores
        user=CustomUser.objects.get(pk=userId) # get userscore
        if str(answerId)==question.correct_answer:  # check answer
            user.score+=question.score_ca  # add score
            print(user.score)
        else: 
            user.score+=question.score_wa  # minus score
            print(user.score)
        user.save()  #save score 
 
        return user.score  #return score

