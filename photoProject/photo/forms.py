from django import forms
from .models import PhotoPost

class SearchForm(forms.Form):
    key = forms.CharField(label='検索文字列')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['key'].widget.attrs['class'] = 'form-control'

class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category','title','comment','image1','image2']
        labels = {
            'category':'カテゴリ',
            'title':'タイトル',
            'comment':'コメント',
            'image1':'イメージ1',
            'image2':'イメージ2',
        }
