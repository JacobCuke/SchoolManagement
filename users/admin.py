from django.contrib import admin
from .models import (
    Profile,
    Student,
    Instructor,
    ExtraCurricular
)

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('user', 'birth_date', 'address')

class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('user', 'year', 'student_id_no')

class InstructorAdmin(admin.ModelAdmin):
    model = Instructor
    list_display = ('user', 'start_date', 'office_number', 'office_phone_number')

class ExtraCurricularAdmin(admin.ModelAdmin):
    model = ExtraCurricular
    list_display = ('user', 'activity_name')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(ExtraCurricular, ExtraCurricularAdmin)
