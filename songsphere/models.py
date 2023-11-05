from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5000)
    singer=models.CharField(max_length=5000)
    tags=models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images')
    song= models.FileField(upload_to='images')
    link=models.CharField(max_length=200,blank=True,null=True)
    lyrics=models.TextField(blank=True,null=True)
    duration=models.CharField(max_length=20)

    def __str__(self):
        return self.name