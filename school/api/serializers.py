from rest_framework import serializers
from school.models import Course
from users.api.serializers import InstructorSerializer

class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'instructor', 'time', 'day']