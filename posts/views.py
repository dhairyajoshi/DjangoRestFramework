from cgi import parse_multipart
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import NotificationSerializer, PostSerializer
from .models import Notification, Post
from accounts.models import NewUser
# Create your views here.


@api_view(['GET'])
def getposts(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= Post.objects.all()


    serialized = PostSerializer(data,many=True)

    return Response(serialized.data)


@api_view(['GET'])
def getpost(request,id):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    data= Post.objects.get(id=id)

    serialized = PostSerializer(data,many=False)

    return Response(serialized.data)


@api_view(['POST'])
def addpost(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    serialized = PostSerializer(data=request.data)

    if serialized.is_valid():
        serialized.save(username= request.user.username,user=request.user,pfp=request.user.pfp)
        user = NewUser.objects.get(username=request.user.username)
        user.posts=user.posts+1
        user.save()

    return Response(serialized.data)


@api_view(['POST'])
def likepost(request,id):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    post = Post.objects.get(id=id)
    sender=request.user

    notifs=Notification.objects.filter(sender=sender,post_id=id)

    if notifs.count()>0:
        post.likes=post.likes-1
        user= NewUser.objects.get(username=post.user.username)
        user.likes= user.likes-1
        user.save()
        post.save() 
        notifs.delete()
        return Response({'msg':'post unliked'})

    post.likes= post.likes+1
    notification = Notification.objects.create(
        sender=sender.username,
        receiver=post.username,
        post=post.caption, 
        pic=post.pic,
        post_id=post.id

    )
 
    # serialized=NotificationSerializer(data=notification)

    
    user= NewUser.objects.get(username=post.user.username)
    user.likes= user.likes+1
    user.save()
    

    post.save() 

    res={"msg":"post liked"}
    return Response(res)

@api_view(['GET'])
def isLiked(request,id):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    sender=request.user

    notifs=Notification.objects.filter(sender=sender,post_id=id)

    if notifs.count()>0:
        return Response({'msg':'1'})

    else:
        return Response({'msg':'0'})

