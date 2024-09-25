from django import forms
from .models import BlogPost

class SearchForm(forms.Form):
    key = forms.CharField(label='検索文字列')

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title","content","category","image"]
        labels = {
            "title":"題名",
            "content":"本文",
            "category":"カテゴリ",
            "image":"画像",
        }