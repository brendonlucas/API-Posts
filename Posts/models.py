from django.db import models
from Profile.models import *


class Post(models.Model):
    title = models.CharField(max_length=350)
    body = models.CharField(max_length=350)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE)


