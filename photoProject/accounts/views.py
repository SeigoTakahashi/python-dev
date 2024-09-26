from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CreateCustomUserForm

class SignUpView(CreateView):
    model = CustomUser											
    template_name ='accounts/signup.html'
    form_class = CreateCustomUserForm
    success_url = reverse_lazy('accounts:signup_success')

class SignUpSuccessView(TemplateView):
    template_name = 'accounts/signup_success.html'

