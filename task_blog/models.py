from django.conf import settings
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    brief_description = models.CharField(max_length=250)
    # image = models.ImageField(null=True, upload_to='images')
    full_description = models.CharField(max_length=350)

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.CharField(max_length=250)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
