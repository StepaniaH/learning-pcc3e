from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Article(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f"{self.title} - {self.body[:50]}..."

