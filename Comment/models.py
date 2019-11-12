from django.db import models
from Posts.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    body = models.CharField(max_length=350)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
