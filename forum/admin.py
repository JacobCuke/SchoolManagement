from django.contrib import admin
from .models import (
    DiscussionThread,
    DiscussionPost
)

class DiscussionThreadAdmin(admin.ModelAdmin):
    model = DiscussionThread
    list_display = ('title', 'course', 'creation_date_time', 'author')

class DiscussionPostAdmin(admin.ModelAdmin):
    model = DiscussionPost
    list_display = ('thread', 'creation_date_time', 'author', 'content')

admin.site.register(DiscussionThread, DiscussionThreadAdmin)
admin.site.register(DiscussionPost, DiscussionPostAdmin)
