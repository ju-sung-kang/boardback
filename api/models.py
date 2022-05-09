from django.db import models

# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.TextField()
    content=models.TextField()
    date=models.DateField()

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    content=models.TextField()
    date=models.DateField()