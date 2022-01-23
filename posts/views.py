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

    if request.user.is_staff:
        data= Post.objects.all().order_by('-date')
        serialized = PostSerializer(data,many=True)

        return Response(serialized.data) 

    data= Post.objects.all().filter(status='p').order_by('-date') | Post.objects.all().filter(username=request.user).order_by('-date') | Post.objects.all().filter(username=request.user).order_by('-date')


    serialized = PostSerializer(data,many=True)

    return Response(serialized.data) 


@api_view(['GET'])
def getpost(request,id):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    data= Post.objects.get(id=id)

    serialized = PostSerializer(data,many=False)

    return Response(serialized.data)

@api_view(['GET'])
def sortedposts(request):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    data= Post.objects.all().order_by('likes')

    serialized=PostSerializer(data,many=True)

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

    return Response({'msg':'Uploaded successfully'})


@api_view(['POST']) 
def likepost(request,id,act):
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})
    post = Post.objects.get(id=id)
    sender=request.user

    notifs=Notification.objects.filter(sender=sender,post_id=id)
    
    

    if(act=='like'):
    
        if notifs.count()>0:

            post.likes=post.likes-1
            user= NewUser.objects.get(username=post.user.username)
            user.likes= user.likes-1
            user.save()
            post.save() 
            notifs.delete()
            last_notif= Notification.objects.filter(post_id=id).order_by('-date').last()
            if last_notif is not None:
                usr= last_notif.sender

            else:
                usr="" 
            return Response({'count':post.likes,'msg':'1','usr':usr})


        post.likes= post.likes+1
        Notification.objects.create(
            sender=sender.username,
            receiver=post.username,
            post=post.caption, 
            pic=post.pic,
            post_id=post.id

        )
            
        user= NewUser.objects.get(username=post.user.username)
        user.likes= user.likes+1
        user.save()
        post.save() 
        last_notif= Notification.objects.filter(post_id=id).order_by('-date').last()
        if last_notif is not None:
            usr= last_notif.sender

        else:
            usr="" 

        res={'count':post.likes,'msg':'0','usr':usr}
        return Response(res)

    if(act=='dt'):
    
        if notifs.count()>0:
            return Response({'count':post.likes,'msg':'1','usr':usr})


        post.likes= post.likes+1
        Notification.objects.create(
            sender=sender.username,
            receiver=post.username,
            post=post.caption, 
            pic=post.pic,
            post_id=post.id

        )
        last_notif= Notification.objects.filter(post_id=id).order_by('-date').last()
        if last_notif is not None:
            usr= last_notif.sender

        else:
            usr="" 
            
        user= NewUser.objects.get(username=post.user.username)
        user.likes= user.likes+1
        user.save()
        post.save() 

        res={'count':post.likes,'msg':'0','usr':usr}
        return Response(res)

    if(act=='chk'):
        last_notif= Notification.objects.filter(post_id=id).order_by('-date').last()
        if last_notif is not None:
            usr= last_notif.sender

        else:
            usr=""


        if notifs.count()>0:
            return Response({'count':post.likes,'msg':'1','usr':usr})

        return Response({'count':post.likes,'msg':'0','usr':usr})


@api_view(['POST'])
def admin_action(request,id,act):

    
    if not request.user.is_authenticated:
        return Response({'error':'user not authenticated'})

    post = Post.objects.get(id=id)

    if not request.user.is_staff:
        if post.username==request.user.username:
            if act=='del':
                likes= post.likes
                user= NewUser.objects.get(username=request.user.username)
                user.likes= user.likes-likes
                user.posts= user.posts-1
                user.save()
                
                post.delete()
                return Response({'msg':'Post deleted'})

            else:
                return Response({'msg':'Nice try, peasant'})

        return Response({'msg':'Nice try, peasant'})

    if act=='del':
        likes= post.likes
        user= NewUser.objects.get(username=post.username)
        user.likes= user.likes-likes
        user.posts= user.posts-1
        user.save()
                
        post.delete()
        return Response({'msg':'Post deleted'})

    if act=='hid':
        if post.status=='p':
            post.status='d'
            post.save()
            return Response({'msg':'Post hidden'})
        
        else:
            post.status='p'
            post.save()
            return Response({'msg':'Post made public'})
        
        

    

    
            
    