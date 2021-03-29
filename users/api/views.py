from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User
from users.models import Student, Instructor
from users.api.serializers import UserSerializer
from school.models import Course, EnrolledIn, AssistsIn
from school.api.serializers import CourseSerializer

@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        users = User.objects.filter(id__in=students)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
def student_enrollments(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        enrollments = EnrolledIn.objects.filter(student=student).values('course')
        courses = Course.objects.filter(id__in=enrollments)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def student_assitances(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        assistances = AssistsIn.objects.filter(student=student).values('course')
        courses = Course.objects.filter(id__in=assistances)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def instructor_list(request):
    if request.method == 'GET':
        instructors = Instructor.objects.all()
        users = User.objects.filter(id__in=instructors)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def instructor_detail(request, pk):
    try:
        instructor = Instructor.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)