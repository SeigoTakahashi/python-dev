from django import forms

class SearchForm(forms.Form):
    key = forms.CharField(label='検索文字列')