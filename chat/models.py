from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


def media_path(instance, filename):
    return f'chat/media/{instance.sender.id}/{instance.receiver.id}/{filename}'



class DirectMessage(models.Model):
    CONTENT_CHOICE = ((1, 'Text'),
                      (2, 'Audio'),
                      (3, 'Image'),
                      (4, 'Video'),)

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content_type = models.IntegerField( choices=CONTENT_CHOICE)
    content = models.FileField(upload_to=media_path, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)

    