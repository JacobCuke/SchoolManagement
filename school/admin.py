from django.contrib import admin
from .models import (
  Course,
  EnrolledIn,
  AssistsIn,
  Lecture,
  Assignment,
  Submission,
  ExtraCurricular,
  Guardian
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

class SubmissionAdmin(admin.ModelAdmin):
    model = Submission
    list_display = ('student', 'assignment', 'grade_report', 'feedback', 'submission_time', 'content')

class ExtraCurricularAdmin(admin.ModelAdmin):
    model = ExtraCurricular
    list_display = ('student', 'activity_name')

class GuardianAdmin(admin.ModelAdmin):
    model = Guardian
    list_display = ('student', 'first_name', 'last_name', 'phone_number', 'address', 'relation')

admin.site.register(Course, CourseAdmin)
admin.site.register(EnrolledIn, EnrolledInAdmin)
admin.site.register(AssistsIn, AssistsInAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(ExtraCurricular, ExtraCurricularAdmin)
admin.site.register(Guardian, GuardianAdmin)
