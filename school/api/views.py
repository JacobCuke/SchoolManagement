from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse

from school.models import Course, EnrolledIn, AssistsIn
from school.api.serializers import CourseSerializer
from users.models import Student, Instructor

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_list(request):
    user = request.user
    instructor = Instructor.objects.filter(user=user).first()

    if not instructor and not user.is_superuser:
        return Response({'message': "Error: you do not have access to this resource"})

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if request.method == 'GET':
        # Determine if request was made by a student or an instructor
        student = Student.objects.filter(user=user).first()
        instructor = Instructor.objects.filter(user=user).first()

        # Request by student
        # Student can't access course unless they are enrolled in or assist in it
        if student:
            if (not EnrolledIn.objects.filter(student=student, course=course).exists() and
                not AssistsIn.objects.filter(student=student, course=course).exists()):
                return Response({'message': "Error: you do not have access to this resource"})

        # Instructors and superusers can access any single course
        else:
            if not instructor and not user.is_superuser:
                return Response({'message': "Error: you do not have access to this resource"})

        serializer = CourseSerializer(course)
        return Response(serializer.data)