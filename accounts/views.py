import email
import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import NewUser
from .serializers import CustomUserSerializer
from posts.serializers import NotificationSerializer
from posts.models import Notification

# Create your views here.

@api_view(['POST'])
def updatePic(request,id):
    
    try:
        user= NewUser.objects.get(id=id)
    except NewUser.DoesNotExist:
        return Response({'msg':'user not found'})

    serialized= CustomUserSerializer(user,data=request.data) 

    if serialized.is_valid():
        serialized.save()

    return Response(serialized.data)  

    
  

@api_view(['POST'])
def registerUser(request):  
    serialized= CustomUserSerializer(data=request.data)

    if serialized.is_valid():
        serialized.save() 

    return Response(serialized.data)


@api_view(['GET'])
def getnotifs(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= Notification.objects.filter(receiver=request.user.username)

    print(data) 

    serialized = NotificationSerializer(data,many=True)

    return Response(serialized.data)