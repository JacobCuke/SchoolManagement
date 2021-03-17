from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Instructor, Student

class Course(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    TIME_CHOICES = [
        (ONE, 'Period 1'),
        (TWO, 'Period 2'),
        (THREE, 'Period 3'),
        (FOUR, 'Period 4'),
        (FIVE, 'Period 5'),
        (SIX, 'Period 6')
    ]

    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    DAY_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday')
    ]

    course_name = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)
    time = models.CharField(max_length=1, blank=True, choices=TIME_CHOICES)
    day = models.CharField(max_length=2, blank=True, choices=DAY_CHOICES)

    def __str__(self):
        return f'{self.course_name} (ID:{self.id})'


class EnrolledIn(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F')
    ]


    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    received_grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True)

    class Meta:
        unique_together = ['student', 'course']

    def __str__(self):
        return f'{self.student} in {self.course}'


class AssistsIn(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['student', 'course']

    def __str__(self):
        return f'{self.student} in {self.course}'


class Lecture(models.Model):
    lecture_title = models.CharField(max_length=255, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    lecture_number = models.PositiveIntegerField()
    content = models.FileField(upload_to='file_uploads', null=True)

    class Meta:
        unique_together = ['course', 'lecture_number']

    def __str__(self):
        return f'Lecture {self.lecture_number}'


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    assignment_number = models.PositiveIntegerField()
    content = models.FileField(upload_to='file_uploads', null=True)

    class Meta:
        unique_together = ['course', 'assignment_number']

    def __str__(self):
        return f'Assignment {self.assignment_number}'


class Submission(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F')
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    grade_report = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True)
    feedback = models.TextField(blank=True)
    submission_time = models.DateTimeField(default=timezone.now)
    content = models.FileField(upload_to='submissions', null=True)

    class Meta:
        unique_together = ['student', 'assignment']

    def __str__(self):
        return f'{self.student} submission for {self.assignment}'


class ExtraCurricular(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ['student', 'activity_name']

    def __str__(self):
        return f'{self.activity_name}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.student.user})


class Guardian(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)

    class Meta:
        unique_together = ['student', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.student.user})
