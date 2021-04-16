from rest_framework import serializers
from school.models import Course, Guardian, ExtraCurricular, Lecture, Assignment,Submission, AssistsIn, EnrolledIn
from users.api.serializers import InstructorSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'instructor', 'time', 'day']

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'lecture_title', 'course', 'due_date', 'lecture_number', 'content']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'course', 'due_date', 'assignment_number', 'content']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['student', 'assignment', 'grade_report', 'feedback', 'submission_time']

class EnrolledInSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolledIn
        fields = ['student', 'course']

class AssistsInSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistsIn
        fields = ['student', 'course']

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'relation']

class ExtraCurricularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraCurricular
        fields = ['activity_name']