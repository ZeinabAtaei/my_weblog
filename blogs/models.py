from django.db import models

from accounts.models import CustomUser


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status =models.CharField(max_length=3, choices=STATUS_CHOICES)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title