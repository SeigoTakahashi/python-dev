from django.http import HttpResponse
from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

