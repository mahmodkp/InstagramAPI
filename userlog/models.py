from django.db import models
from django.contrib.auth import get_user_model

from content.models import Post,Story
User = get_user_model()
# Create your models here.

User = get_user_model()


class PostLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='userlogs')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="postlog")
    action = models.CharField('Content', max_length=50, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"{self.user.username} {self.user.action} {self.post.id} from {self.post.user.username}"

    class Meta:
        ordering = ("-created_at",)


class StoryLog(models.Model):
    user = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name='userlogs')
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name="postlog")
    action = models.CharField('Content', max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user.username} {self.user.action} {self.Story.id} from {self.story.user.username}"

    class Meta:
        ordering = ("-created_at",)

