from django import forms

from comments.models import Commentaries


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Commentaries
        fields = ["body"]
