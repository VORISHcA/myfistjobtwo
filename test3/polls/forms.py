from django import forms

from .models import Topics


class PostForm(forms.ModelForm):

    class Meta:
        model = Topics
        fields = ('topic_text',)


class GetForm(forms.ModelForm):

    class Meta:
        model = Topics
        fields = ('topic_text',)
