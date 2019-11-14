from django.urls import path
from Posts.views import *

urlpatterns = [

    path('posts/', Postlist.as_view(), name=Postlist.name),
    path('posts/<int:pk>', PostDetail.as_view(), name=PostDetail.name),
    path('posts-comments/', PostCommentslist.as_view(), name=PostCommentslist.name),
    path('posts-comments/<int:pk>', PostCommentsDetail.as_view(), name=PostCommentsDetail.name)
]