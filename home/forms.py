# Forms for handling the news items on the main page and the user profile views

from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from .models import NewsPost, UserProfile


class NewsForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['title', 'post']
        exclude = ("author", "time")
        labels = {
            'title': "Title",
            'post': 'Content'
        }
        widgets = {
            'title': widgets.Textarea(attrs={'cols': 50, 'rows': 1, 'class': 'form-control'}),
            'post': widgets.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-control'}),
        }

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("__all__")

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ("__all__")