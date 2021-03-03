from django.contrib import admin
from .models import (
  Course,
  Lecture,
  Assignment,
  EnrolledIn,
  AssistsIn,
  ExtraCurricular
)

class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('id', 'course_name', 'instructor', 'time', 'day')

class EnrolledInAdmin(admin.ModelAdmin):
    model = EnrolledIn
    list_display = ('student', 'course', 'received_grade')

class AssistsInAdmin(admin.ModelAdmin):
    model = AssistsIn
    list_display = ('student', 'course')

class LectureAdmin(admin.ModelAdmin):
    model = Lecture
    list_display = ('id', 'lecture_title', 'course', 'due_date', 'lecture_number', 'content')

class AssignmentAdmin(admin.ModelAdmin):
    model = Assignment
    list_display = ('id', 'course', 'due_date', 'assignment_number', 'content')

class ExtraCurricularAdmin(admin.ModelAdmin):
    model = ExtraCurricular
    list_display = ('user', 'activity_name')

admin.site.register(Course, CourseAdmin)
admin.site.register(EnrolledIn, EnrolledInAdmin)
admin.site.register(AssistsIn, AssistsInAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(ExtraCurricular, ExtraCurricularAdmin)
