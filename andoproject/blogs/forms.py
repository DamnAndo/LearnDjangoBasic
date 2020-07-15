from django.forms import ModelForm
from .models import Comment
from  django import forms
from  django.core import validators

class CommentForm(ModelForm):

    desc = forms.CharField(required=True,widget=forms.Textarea,
                           validators=[validators.MinLengthValidator(5)])

    class Meta:
        model = Comment
        fields = ['desc']
