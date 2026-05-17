from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(
    upload_to='profile_pictures/',
    blank=True,
    null=True
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username


class Story(models.Model):

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('completed', 'Completed')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stories'
    )

    title = models.CharField(
        max_length=255
    )

    synopsis = models.TextField()

    cover_image = models.ImageField(
        upload_to='story_covers/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    views = models.PositiveIntegerField(
        default=0
    )

    votes = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Chapter(models.Model):

    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name='chapters'
    )

    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    chapter_number = models.PositiveIntegerField()

    views = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['chapter_number']
        unique_together = ['story', 'chapter_number']

    def __str__(self):
        return f"{self.story.title} - Chapter {self.chapter_number}"