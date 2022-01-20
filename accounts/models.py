from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, first_name, password, **other_fields)

    def create_user(self, username, first_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not username:
            raise ValueError(_('You must provide an username'))

        user = self.model(username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

def  upload_to_pfp(instance,filename):
    return 'pfps/{filename}'.format(filename=filename)

def  upload_to_cfp(instance,filename):
    return 'cfps/{filename}'.format(filename=filename)

class NewUser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=150, unique=True)
    bio= models.TextField(default="")
    first_name = models.CharField(max_length=150, blank=True)
    pfp= models.ImageField(_("Image"),upload_to=upload_to_pfp,default='pfps/default.jpg')
    cfp= models.ImageField(_("Image"),upload_to=upload_to_cfp,default='cfps/default.jpg')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    posts= models.IntegerField(default=0)
    likes= models.IntegerField(default=0)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']
    

    def __str__(self): 
        return self.username