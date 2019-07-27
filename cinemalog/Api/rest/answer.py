from rest_framework.decorators import APIView
from rest_framework.response import Response
#classes and Functions
from cinemalog.models import UserAnswer,Question
from cinemalog.Api.rest.serializers import UserAnswerSerializer
from users.models import CustomUser
class RegisterAnswer(APIView):
    def get(self,request,format=None):
        pass
    def post(self,request,format=None):  # get answers jason
        #try:
            userScore=0 # define local score
            userId=request.query_params.get('userid')   #split json
            data=request.data['answers']
            #print(data['answers'])
            for item in data:
                comptId=item['cycle_question_id']
                for x in item['data']:
                    questionId=x['question']
                    answerId=x['answer']
                    try:
                        userAnswer=UserAnswer.objects.filter(competition_id=comptId, # check if save before or not 
                        # yani faghat yekbar mitavanad javab dahad
                                    user_id=userId)
                        break     # if save exit compelatly of for
                    except UserAnswer.DoesNotExist:
                        userAnswer=UserAnswer(competition_id=comptId, # if is not save before add
                                    question_id=questionId,
                                    answer=answerId,
                                    user_id=userId)
                        userAnswer.save()  # save
                        userScore=calculateScore(userId,questionId,answerId) # calculate user score
          #          except Exception:
         #               raise Exception("couldnt import,wrong information")
        #except Exception:
        #    raise Exception("key is invalid")
            return Response(userScore)  # return user score


def calculateScore(userId,questionId,answerId):  # calculate user score
        question=Question.objects.get(pk=questionId) # get question scores
        user=CustomUser.objects.get(pk=userId) # get userscore
        if answerId==question.correct_answer:  # check answer
            user.score+=question.score_ca  # add score
            print(user.score)
        else: 
            user.score+=question.score_wa  # minus score
            print(user.score)
        user.save()  #save score 
 
        return user.score  #return score
