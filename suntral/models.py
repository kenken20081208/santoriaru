from django.db import models

class Post(models.Model):
    character = models.CharField(max_length=200)
