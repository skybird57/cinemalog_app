from django.http import HttpResponse,JsonResponse # use in returns
from django.views.decorators.csrf import csrf_exempt # use befor defs for security
from rest_framework.parsers import JSONParser # use to parse json
from cinemalog.Api.rest.permissions import check_permissions
from cinemalog.Api.rest import json_api


import base64
from django.contrib.auth import authenticate

def header_auth_view(request):
    auth_header = request.META['HTTP_AUTHORIZATION']
    encoded_credentials = auth_header.split(' ')[1]  # Removes "Basic " to isolate credentials
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
    username = decoded_credentials[0]
    password = decoded_credentials[1]
    feed_bot = authenticate(username=username, password=password)
    return feed_bot
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
        if True: #check_permissions(request.user,'cinemalog.add_applicationversion'):
            data=JSONParser().parse(request)
            data=json_api.json_create(data)
            return JsonResponse(data,safe=False)
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
        data=json_api.json_update(data,pk)
        return JsonResponse(data,safe=False)
    elif request.method=='DELETE':
        data= json_api.json_delete(request,pk)
        return JsonResponse(data,safe=False)
