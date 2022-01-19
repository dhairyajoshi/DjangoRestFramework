# Django Rest Framework
## Rest api for social media app
This repo contains the api part of the social media app having features to add new post, getting all the posts, liking a post and sending a notification on liking a post.

## Endpoints

add post- http://localhost:8000/post/addpost (get)
get posts- http://localhost:8000/post/getposts (post)
register new user- http://localhost:8000/users/register/ (post)
login user- http://localhost:8000/users/login/ (post)
update profile picture- http://localhost:8000/users/updatepic/ (post)
like post- http://http://localhost:8000/post/likepost/post_id (post)
get notifications- http://localhost:8000/users/getnotifs (get)
get current user- http://localhost:8000/users/getinfo (get)

include authorization token in headers: Bearer <token>

