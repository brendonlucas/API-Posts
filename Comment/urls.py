from django.urls import path

from Comment import views
from Comment.views import *

urlpatterns = [
    path('posts/<int:pk>/comments/', CommentsPostlist.as_view(), name=CommentsPostlist.name),
    path('posts/<int:id_post>/comments/<int:id_comment>/', views.comments_post_detail, name='comment-post-detail')
]

