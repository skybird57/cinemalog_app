from users.models import CustomUser,CustomUserToken

# false means: user or token is invalid
# true means: user and token are valid
def checkUserToken(userid,token):
    try:
        user_instance=CustomUser.objects.get(id=userid)
    except CustomUser.DoesNotExist:
        return False
    try:
        token_instance=CustomUserToken.objects.get(user_id=user_instance.id)
        if token==token_instance.token:
            return True
        else:
            return False
    except CustomUserToken.DoeaNotExist:
        return False