from django.db import models
from django.contrib.auth import get_user_model

from content.models import Post,Story
User = get_user_model()
# Create your models here.

User = get_user_model()


class PostView(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='postview')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="postlog")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} seen post {self.post.id} from {self.post.user.username}"

    class Meta:
        ordering = ("-created_at",)


class StoryView(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='storyview')
    story = models.ForeignKey(
        Story, on_delete=models.CASCADE, related_name="storylog")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} seen story {self.story.id} from {self.story.user.username}"

    class Meta:
        ordering = ("-created_at",)


