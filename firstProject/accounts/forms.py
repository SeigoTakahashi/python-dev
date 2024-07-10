from django import forms

class CreateCustomUserForm(forms.Form):
    username = forms.CharField(label='ユーザー名')
    email = forms.EmailField(label='メールアドレス')
    password1 = forms.CharField(label='パスワード',widget=forms.PasswordInput())
    password2 = forms.CharField(label='パスワード（確認用）',widget=forms.PasswordInput())
