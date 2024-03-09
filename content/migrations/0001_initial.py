# Generated by Django 4.2 on 2024-03-02 13:40

import content.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hashtag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "posted_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Post_posted_time"
                    ),
                ),
                (
                    "caption",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Caption"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Location"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("hashtags", models.ManyToManyField(blank=True, to="content.hashtag")),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="Post_Likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "mentions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="Post_Mentions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "media",
                    models.FileField(
                        null=True, upload_to=content.models.media_file_path
                    ),
                ),
                (
                    "media_type",
                    models.IntegerField(
                        choices=[(1, "image"), (2, "video"), (3, "audio")], null=True
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="content.post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=2000, verbose_name="Content")),
                (
                    "posted_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Comment_posted_time"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Comment_Author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="Comment_Likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Comment_from_Post",
                        to="content.post",
                    ),
                ),
            ],
        ),
    ]
