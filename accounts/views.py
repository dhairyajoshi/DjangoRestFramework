import email
import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import NewUser
from .serializers import CustomUserSerializer

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