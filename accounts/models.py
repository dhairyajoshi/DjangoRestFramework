from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, email, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, email, first_name, password, **other_fields)

    def create_user(self, username, email, first_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        if not email:
            raise ValueError(_('You must provide an email address'))

        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        email = self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user

def  upload_to_pfp(instance,filename):
    return 'pfps/{filename}'.format(filename=filename)

class NewUser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    pfp= models.ImageField(_("Image"),upload_to=upload_to_pfp,default='pfps/default.jpg')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']
    

    def __str__(self): 
        return self.username