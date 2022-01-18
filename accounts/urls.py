from django.urls import path
from . import views

urlpatterns=[
    path('updatepic/<int:id>',views.updatePic),
    path('register/',views.registerUser)
]