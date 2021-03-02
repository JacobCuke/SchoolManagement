from django.db import models
from django.contrib.auth.models import User
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

    course_name = models.CharField(max_length=150)
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)
    time = models.CharField(max_length=1, blank=True, choices=TIME_CHOICES)
    day = models.CharField(max_length=2, blank=True, choices=DAY_CHOICES)

    def __str__(self):
        return f'{self.course_name}(ID:{self.id})'


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
    lecture_title = models.CharField(max_length=150, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    lecture_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ['course', 'lecture_number']

    def __str__(self):
        return f'Lecture {self.lecture_number} of {self.course}'


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    assignment_number = models.PositiveIntegerField()

    class Meta:
        unique_together = ['course', 'assignment_number']

    def __str__(self):
        return f'Assignment {self.assignment_number} of {self.course}'
