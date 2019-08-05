import graphene

#classes and funstions
from cinemalog.models import Question,UserAnswer
from users.models import CustomUser
from cinemalog.Api.GraphQL.types import UserAnswerType
from users.Api.Rest.checkUserToken import checkUserToken
class RegisterAnswer(graphene.Mutation):
    userAnswer=graphene.Field(UserAnswerType)
    class Arguments:
        userId=graphene.Int()
        token=graphene.String()
        answer=graphene.JSONString()

    def mutate(self,info,userId,token,answer):
        if not checkUserToken(userId,token):
            raise Exception("user id or token is invalid")
        answer=answer['answers']
        userScore=0
        for item in answer:
            print('item=',item)
            comptId=item['cycle_question_id']
            try:
                userAnswer_instance=UserAnswer.objects.filter(competition_id=comptId,user_id=userId)
                # check if save before or not 
                # yani faghat yekbar mitavanad javab dahad
                print('useridddddd',userAnswer_instance[0].user_id)
                break     # if save before exit compelatly of for
            except IndexError:
                for x in item['data']:
                    print('x=',x)
                    questionId=x['question']
                    answerId=x['answer']
                    try:  #check is compId and questionId are related
                        question=Question.objects.get(pk=questionId,competition_id=comptId)
                    except Exception:
                        raise Exception("competition info is not matched with question info")
                    
                    try:    # try to add record
                        userAnswer_instance=UserAnswer(competition_id=comptId, # if is not save before add
                                question_id=questionId,
                                answer=answerId,
                                user_id=userId)
                        userAnswer_instance.save()  # save
                        userScore=calculateScore(userId,questionId,answerId) # calculate user score
                        userAnswer_instance.message=str(userScore)
                        print('userScore  ',userScore)
                        return RegisterAnswer(userAnswer=userAnswer_instance)
                    except Exception:
                        raise Exception("couldnt import,wrong information")
 

class Mutation(graphene.ObjectType):
    registerAnswer=RegisterAnswer.Field()


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
