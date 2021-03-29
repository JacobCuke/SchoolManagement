from rest_framework import serializers
from school.models import Course, Guardian, ExtraCurricular
from users.api.serializers import InstructorSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'instructor', 'time', 'day']

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'relation']

class ExtraCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCurricular
        fields = ['activity_name']