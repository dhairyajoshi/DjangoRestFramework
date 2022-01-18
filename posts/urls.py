from django.urls import path
from . import views


urlpatterns=[
    path('getposts',views.getposts),
    path('getposts/<int:id>',views.getpost),
    path('addpost',views.addpost),
    path('likepost/<int:id>',views.likepost)
]
