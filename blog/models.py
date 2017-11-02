from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Blog_data(models.Model):
    text = models.CharField(max_length=200)
    link = models.URLField()

    def publish(self):
        self.save()

    #제목을 링크의 주소로
    def __str__(self):
        return self.text



    