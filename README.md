# Django Rest Framework
## Rest api for social media app
This repo contains the api part of the social media app having features to add new post, getting all the posts, liking a post and sending a notification on liking a post.

## Endpoints

add post- /post/addpost (get) <br/>
get posts- /post/getposts (post) <br/>
register new user- /users/register/ (post) <br/>
login user- /users/login/ (post) <br/>
update profile picture- /users/updatepic/ (post) <br/>
like post- /post/likepost/post_id (post) <br/>
get notifications- /users/getnotifs (get) <br/>
get current user- /users/getinfo (get) <br/>

include authorization token in headers: Bearer _token_

