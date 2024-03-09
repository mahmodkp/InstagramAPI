
from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey('content.Post',
                             related_name='Comment_from_Post',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='Comment_Author',
                               on_delete=models.CASCADE)
    content = models.CharField('Content', max_length=2000, blank=False)
    # usertags = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                                   related_name='Comment_Tags',
    #                                   blank=True,
    #                                   symmetrical=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Comment_Likes",
                                   blank=True,
                                   symmetrical=False)
    posted_time = models.DateTimeField(
        'Comment_posted_time', auto_now_add=True)

    def __str__(self):
        return "{}'s comment in {}".format(self.author, self.post)

    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='Owner',
                               on_delete=models.CASCADE)
    posted_time = models.DateTimeField('Post_posted_time', auto_now_add=True)
    caption = models.CharField(
        'Caption', max_length=200, blank=True, null=True)
    location = models.CharField('Location', max_length=50, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Post_Likes",
                                   blank=True,
                                   symmetrical=False)
    # usertags = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                                   related_name='Post_Tags',
    #                                   blank=True,
    #                                   symmetrical=True)
    hashtags = models.ManyToManyField('content.Hashtag',
                                      # related_name='Post_Hashags',
                                      blank=True,
                                      symmetrical=True)
    mentions = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name="Post_Mentions",
                                      blank=True,
                                      symmetrical=False)

    def __str__(self):
        return "{}'s post({})".format(self.author, self.pk)

    def comments(self):
        ''' Get all comments '''
        return Comment.objects.filter(post__id=self.pk)

    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0

    def get_likes(self):
        post = self.get_object()
        return post.likes()

class Story(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='Story_Owner',
                               on_delete=models.CASCADE)
    posted_time = models.DateTimeField('Story_posted_time', auto_now_add=True)
    caption = models.CharField(
        'Caption', max_length=200, blank=True, null=True)
    location = models.CharField('Location', max_length=50, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Story_Likes",
                                   blank=True,
                                   symmetrical=False)
    # usertags = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                                   related_name='Post_Tags',
    #                                   blank=True,
    #                                   symmetrical=True)
    hashtags = models.ManyToManyField('content.Hashtag',
                                      # related_name='Post_Hashags',
                                      blank=True,
                                      symmetrical=True)
    mentions = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      related_name="Story_Mentions",
                                      blank=True,
                                      symmetrical=False)

    def __str__(self):
        return "{}'s post({})".format(self.author, self.pk)

    def comments(self):
        ''' Get all comments '''
        return Comment.objects.filter(post__id=self.pk)

    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0

    def get_likes(self):
        post = self.get_object()
        return post.likes()

class Hashtag(models.Model):
    name = models.CharField("Name", max_length=100, blank=False, unique=True)

    def related_posts(self):
        return Post.objects.filter(hashtags__id=self.pk)


def media_file_path(instance, filename):
    """
    Get file path for media
    """
    return f"content/media/{instance.id}/{filename}"


class Media(models.Model):
    FILE_CHOICES = (
        (1, 'image'),
        (2, 'video'),
        (3, 'audio'),
    )
    post = models.ForeignKey(
        Post,
        related_name='media',
        on_delete=models.CASCADE,
    )
    media = models.FileField(upload_to=media_file_path,
                             null=True)
    media_type = models.IntegerField(
        choices=FILE_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
