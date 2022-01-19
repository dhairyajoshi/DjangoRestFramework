from django.urls import path
from . import views

urlpatterns=[
    path('updatepic/',views.updatePic),
    path('register/',views.registerUser),
    path('getnotifs',views.getnotifs),
    path('login/',views.loginUser),
    path('getinfo',views.getinfo)
]