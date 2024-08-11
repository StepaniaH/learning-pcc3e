from django import forms

from .models import Blog, Article

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'pub_date']
        labels = {
            'title': '',
            'pub_date': '',
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'pub_date']
        labels = {
            'title': '',
            'body': '',
            'pub_date': '',
        }
