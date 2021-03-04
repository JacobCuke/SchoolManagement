from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from school.models import Course

class DiscussionThread(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    creation_date_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'


class DiscussionPost(models.Model):
    thread = models.ForeignKey(DiscussionThread, on_delete=models.CASCADE)
    creation_date_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()

    def __str__(self):
        return f'Post ID: {self.id} in {self.thread}'