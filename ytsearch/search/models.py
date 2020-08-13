from django.db import models

# Create your models here.
class SavedVids(models.Model):
    videoId = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    publishedAt = models.DateTimeField()
    thumbnails_url = models.CharField(max_length=200)