from collections import OrderedDict
from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Student, Instructor, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['birth_date', 'address']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['year', 'student_id_no']


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['start_date', 'office_number', 'office_phone_number']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    student = StudentSerializer(required=False)
    instructor = InstructorSerializer(required=False)
    password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'profile', 'student', 'instructor']
        extra_kwargs = {'password': {'write_only': True}}

    def to_representation(self, value):
        representation = super(UserSerializer, self).to_representation(value)
        return OrderedDict((k, v) for k, v in representation.items() if v is not None)

    def validate(self, data):
        if not data.get('student', None) and not data.get('instructor', None):
            raise serializers.ValidationError("You must specify if user is a student or an instructor")
        if data.get('student', None) and data.get('instructor', None):
            raise serializers.ValidationError("User cannot be both a student and an instructor")
        return data

    def create(self, validated_data):
        profile_data = None
        student_data = None
        instructor_data = None
        password = None

        if validated_data.get('profile', None):
            profile_data = validated_data.pop('profile')
        if validated_data.get('student', None):
            student_data = validated_data.pop('student')
        if validated_data.get('instructor', None):
            instructor_data = validated_data.pop('instructor')

        # Set password to default 'testing321' if none provided
        if validated_data.get('password', None):
            password = validated_data.pop('password')
        else:
            password = 'testing321'

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        if profile_data:
            if profile_data.get('birth_date', None):
                user.profile.birth_date = profile_data.get('birth_date')
            if profile_data.get('address', None):
                user.profile.address = profile_data.get('address')
            user.save()

        if instructor_data:
            Instructor.objects.create(user=user, **instructor_data)

        if student_data:
            Student.objects.create(user=user, **student_data)

        return user