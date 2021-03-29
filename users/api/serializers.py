from collections import OrderedDict
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Student, Instructor, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['birth_date', 'address']


class StudentSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Student
        fields = ['year', 'student_id_no']


class InstructorSerializer(serializers.ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Instructor
        fields = ['start_date', 'office_number', 'office_phone_number']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    student = StudentSerializer()
    instructor = InstructorSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile', 'student', 'instructor']

    def to_representation(self, value):
        representation = super(UserSerializer, self).to_representation(value)
        return OrderedDict((k, v) for k, v in representation.items() if v is not None)