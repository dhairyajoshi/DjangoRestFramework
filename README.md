# Django Rest Framework
## Rest api for social media app
This repo contains the api part of the social media app having features to add new post, getting all the posts, liking a post and sending a notification on liking a post.

## Endpoints

add post- http://localhost:8000/post/addpost (get) <br/>
get posts- http://localhost:8000/post/getposts (post) <br/>
register new user- http://localhost:8000/users/register/ (post) <br/>
login user- http://localhost:8000/users/login/ (post) <br/>
update profile picture- http://localhost:8000/users/updatepic/ (post) <br/>
like post- http://http://localhost:8000/post/likepost/post_id (post) <br/>
get notifications- http://localhost:8000/users/getnotifs (get) <br/>
get current user- http://localhost:8000/users/getinfo (get) <br/>

include authorization token in headers: Bearer _token_

