from rest_framework import serializers
from forum.models import DiscussionThread, DiscussionPost

class DiscussionThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionThread
        fields = ['id', 'title', 'course', 'creation_date_time', 'author']
        read_only_fields = ['creation_date_time']


class DiscussionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionPost
        fields = ['id', 'thread', 'creation_date_time', 'author', 'content']
        read_only_fields = ['creation_date_time']