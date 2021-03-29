from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile' 


class Student(models.Model):
    GRADE_TEN = '10'
    GRADE_ELEVEN = '11'
    GRADE_TWELVE = '12'
    YEAR_CHOICES = [
        (GRADE_TEN, '10th Grade'),
        (GRADE_ELEVEN, '11th Grade'),
        (GRADE_TWELVE, '12th Grade')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)
    student_id_no = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.student_id_no})'


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    start_date = models.DateField()
    office_number = models.CharField(max_length=10, blank=True)
    office_phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
