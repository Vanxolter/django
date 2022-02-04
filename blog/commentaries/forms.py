
from django import forms

from commentaries.models import Commentaries


class CommentariesForm(forms.ModelForm):
    class Meta:
        model = Commentaries
        fields = ['text']