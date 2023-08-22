from django.db import models
from django.contrib.auth.models import User

# Create your models here

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    content_data = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)  

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)