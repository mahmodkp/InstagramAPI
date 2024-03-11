
from .models import Post, Story
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from userlog.models import PostLog,StoryLog
User = get_user_model()

@receiver(post_save, sender=Post)
def create_post(sender, instance, created, **kwargs):
    if created:

        print('****************')
        print('Post created!')
        print('****************')
        PostLog.objects.create(user=instance.author,
                               post=instance, action="create post")


@receiver(post_save, sender=Story)
def create_post(sender, instance, created, **kwargs):
    if created:
        print('****************')
        print('Story created!')
        print('****************')
        PostLog.objects.create(user=instance.author,
                               post=instance, action="create story")


