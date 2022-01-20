from django.urls import path
from . import views

urlpatterns=[
    path('updateprofile/',views.updateProfile),
    path('register/',views.registerUser),
    path('getnotifs',views.getnotifs),
    path('login/',views.loginUser),
    path('getinfo',views.getinfo)
]