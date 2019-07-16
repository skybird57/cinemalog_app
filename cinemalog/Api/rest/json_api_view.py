from django.http import HttpResponse,JsonResponse # use in returns
from django.views.decorators.csrf import csrf_exempt # use befor defs for security
from rest_framework.parsers import JSONParser # use to parse json
from cinemalog.Api.rest.permissions import check_permissions
from cinemalog.Api.rest import json_api



def index(request):

    html=''
    html+='<a href={}>ApplicationVersion_list</a></br>'.format("/cinemalog/api/video_list")
    html+='<a href={}>ApplicationVersion_create</a></br>'.format("/cinemalog/api/video_create")
    html+='<a href={}>ApplicationVersion_detial</a></br>'.format("/cinemalog/api/video_detail/1/")

    return HttpResponse(html)

@csrf_exempt
def json_list(request):
    """
    List all Videos, or create a new Video.
    """
    
    if request.method=='GET':    
        data=json_api.json_list()
        return JsonResponse(data,safe=False)
    
    elif request.method=='POST':
        return HttpResponse(request)
        data=JSONParser().parse(request)
        return HttpResponse(data)
        if check_permissions(request.user,'cinemalog.add_applicationversion'):
            data=JSONParser().parse(request)
            #data=json_api.json_create(data,request.user)
            return JsonResponse(request.user,safe=False)
        return JsonResponse('Dont have permission to add')  

@csrf_exempt
def json_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    if request.method=='GET':
        data=json_api.json_detail(pk)
        return JsonResponse(data,safe=False)

    elif request.method=='PUT':
        data=JSONParser().parse(request)
        data=json_api.json_update(data,request.user,pk)
        return JsonResponse(data,safe=False)
    elif request.method=='DELETE':
        data= json_api.json_delete(request,pk)
        return JsonResponse(data,safe=False)
