from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse

from forum.api.serializers import DiscussionThreadSerializer, DiscussionPostSerializer
from django.contrib.auth.models import User
from forum.models import DiscussionThread, DiscussionPost
from school.models import Course, EnrolledIn, AssistsIn
from users.models import Student, Instructor

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def thread_list(request, **kwargs):
    user = request.user
    # Try to get the course
    try:
        course = Course.objects.get(pk=kwargs.get('course_id'))
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # PERMISSIONS

    # Determine if request was made by a student or an instructor
    student = Student.objects.filter(user=user).first()
    instructor = Instructor.objects.filter(user=user).first()

    # Student can't access course discussion unless they are enrolled in the course or assist in it
    if student:
        if (not EnrolledIn.objects.filter(student=student, course=course).exists() and
            not AssistsIn.objects.filter(student=student, course=course).exists()):
            return Response({'message': "Error: you do not have access to this resource"}, status=status.HTTP_403_FORBIDDEN)
    # Instructors can access discussion boards of courses they teach
    elif instructor:
        if instructor != course.instructor:
            return Response({'message': "Error: you do not have access to this resource"}, status=status.HTTP_403_FORBIDDEN)
    # Superusers can access any course
    else:
        if not user.is_superuser:
            return Response({'message': "Error: you do not have access to this resource"}, status=status.HTTP_403_FORBIDDEN)

    # END PERMISSIONS

    if request.method == 'GET':
        threads = DiscussionThread.objects.filter(course=course)
        serializer = DiscussionThreadSerializer(threads, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DiscussionThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': "TO DO"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request, course_id, pk):
    # TO DO
    return Response({'message': "TO DO"}, status=status.HTTP_200_OK)