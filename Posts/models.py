from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=255)
    date_posted = models.DateField()

    def __str__(self):
        return self.text

class Message(models.Model):
    datetime_posted = models.DateTimeField()
    response = models.CharField(max_length=10)
    likes = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'Message created by {self.user.username} on {self.datetime_posted}'