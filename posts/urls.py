from django.urls import path
from . import views


urlpatterns=[
    path('getposts',views.getposts),
    path('getposts/<int:id>',views.getpost),
    path('sortedposts',views.sortedposts),
    path('addpost',views.addpost),
    path('likepost/<int:id>',views.likepost),
    path('isliked/<int:id>',views.isLiked)
]
