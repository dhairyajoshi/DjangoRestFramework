from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.

def  upload_to_post(instance,filename):
    return 'posts/{filename}'.format(filename=filename)

def  upload_to_notif(instance,filename):
    return 'notifs/{filename}'.format(filename=filename)
    

class Post(models.Model):

    caption= models.CharField(max_length=150)
    username= models.CharField(max_length=150,default="none")
    user= models.ForeignKey(
        settings.AUTH_USER_MODEL ,on_delete=models.CASCADE,default=None
    )
    pic= models.ImageField(_("Image"),upload_to=upload_to_post,default='posts/default.jgp')
    likes= models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption 


class Notification(models.Model):
    sender= models.CharField(max_length=150,default='none')
    receiver= models.CharField(max_length=150,default='none')
    post = models.CharField(max_length=150,default='none')
    pic= models.ImageField(_("Image"),upload_to=upload_to_notif,default='notifs/default.jpg')
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.sender} liked {self.receiver}\'s post'


         