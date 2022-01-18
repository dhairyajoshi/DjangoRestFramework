from django.urls import path
from . import views

urlpatterns=[
    path('updatepic/<int:id>',views.updatePic),
    path('register/',views.registerUser),
    path('getnotifs',views.getnotifs),
    path('getinfo',views.getinfo)
]