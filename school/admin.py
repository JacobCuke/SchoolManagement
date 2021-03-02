from django.contrib import admin
from .models import (
  Course,
  Lecture,
  EnrolledIn,
  AssistsIn
)

class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('id', 'course_name', 'instructor', 'time', 'day')

class LectureAdmin(admin.ModelAdmin):
    model = Lecture
    list_display = ('id', 'lecture_title', 'course', 'due_date', 'lecture_number')

class EnrolledInAdmin(admin.ModelAdmin):
    model = EnrolledIn
    list_display = ('student', 'course', 'received_grade')

class AssistsInAdmin(admin.ModelAdmin):
    model = AssistsIn
    list_display = ('student', 'course')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(EnrolledIn, EnrolledInAdmin)
admin.site.register(AssistsIn, AssistsInAdmin)
