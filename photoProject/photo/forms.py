from django import forms

class SearchForm(forms.Form):
    key = forms.CharField(label='検索文字列')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['key'].widget.attrs['class'] = 'form-control'