from django import forms
from .models import DiscussionThread, DiscussionPost

class ThreadForm(forms.ModelForm):
    title = forms.CharField(max_length=255)

    class Meta:
        model = DiscussionThread
        fields = ['title']


class PostForm(forms.ModelForm):
    
    class Meta:
        model = DiscussionPost
        fields = ['content']