from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from django.urls import reverse_lazy
from .forms import CreateCustomUserForm
from .models import CustomUser

class SignUpView(FormView):
    template_name = 'accounts/signup.html'
    form_class = CreateCustomUserForm
    success_url = reverse_lazy("blog:index")

    def form_valid(self,form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password1 = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        print(username,email,password1,password2)
        return super().form_valid(form)


