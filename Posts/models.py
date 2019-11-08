from django.db import models
from Profile.models import *


class Post(models.Model):
    title = models.CharField(max_length=350)
    body = models.CharField(max_length=350)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        unique_together = ['id', 'title', 'body']
        ordering = ['id']

    def __str__(self):
        return 'id: %d : %s :%s' % (self.id, self.title, self.body)
