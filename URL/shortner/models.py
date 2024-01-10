from django.db import models

# Create your models here.

class Urls(models.Model):
    url = models.URLField()
    shortenedURL = models.TextField()

    def __str__(self):
        return self.url
