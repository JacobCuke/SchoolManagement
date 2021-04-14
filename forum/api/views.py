from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse

from forum.api.serializers import DiscussionThreadSerializer, DiscussionPostSerializer
from django.contrib.auth.models import User
from school.models import Course

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def thread_list(request):
    # TO DO
    return Response({'message': "TO DO"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    # TO DO
    return Response({'message': "TO DO"}, status=status.HTTP_200_OK)