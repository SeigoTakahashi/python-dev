from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CreateCustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username","email","password1","password2"]
        labels = {
            "username":"ユーザー名",
            "email":"メールアドレス",
            "password1":"パスワード",
            "password2":"パスワード（確認用）",
        }
