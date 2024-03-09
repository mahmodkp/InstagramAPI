from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from .managers import CustomUserManager
from django.conf import settings

# class CustomUser1(AbstractUser):
#     """
#     New model for user. authentication and saving attributes
#     of user i in this moedel.
#     """
#     email = models.EmailField(_('email address'), unique=True)
#     mobile = models.CharField(_("mobile number"), max_length=50)
#     address = models.CharField(_("adress"), max_length=400)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('username',)

#     objects = CustomUserManager()

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


class CustomUser(AbstractUser):
    ''' User Model '''
    first_name = models.CharField('First Name', max_length=60)
    last_name = models.CharField('Last Name', max_length=60)
    username = models.CharField('Username', max_length=30, unique=True)
    email = models.EmailField('Email', max_length=150, unique=True)
    mobile = models.CharField(
        'Phone Number', blank=True, null=True, unique=True)
    bio = models.TextField('Bio', blank=True, null=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    profile_pic = models.ImageField('Profile Picture',
                                    upload_to='user/media/',
                                    default='user/user.png')
    gender = models.IntegerField('Gender',
                                 null=True,
                                 choices=[(1, 'Male'), (2, 'Female')])
    # account_type = models.IntegerField('Account Type',
    #                                    default=1,
    #                                    choices=[(1, 'Private'), (2, 'Public')])
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='Follower',
                                       blank=True,
                                       symmetrical=False)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='Following',
                                       blank=True,
                                       symmetrical=False)
    show_activity_status = models.BooleanField(default=True)
    allow_sharing = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    is_deactivated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    reg_token = models.IntegerField(
        'Registration Token', blank=True, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def followers_count(self):
        ''' No of followers '''
        if self.followers.count():
            return self.followers.count()
        return 0

    def following_count(self):
        ''' No of following '''
        if self.following.count():
            return self.following.count()
        return 0

    def post_count(self):
        ''' No of posts '''
        if self.post_set.count():
            return self.post_set.count()
        return 0

    def posts(self):
        ''' Get all the posts '''
        return Post.objects.filter(author__id=self.pk)

    def tagged_posts(self):
        ''' Get all tagged in posts '''
        return Post.objects.filter(tags__id=self.pk)
