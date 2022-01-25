from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.ImageField(required=False)
    slug = forms.SlugField()
    text = forms.CharField(max_length=2000, help_text='Введите ваш текст')