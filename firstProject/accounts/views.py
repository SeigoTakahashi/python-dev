from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import CreateCustomUserForm

class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = CreateCustomUserForm()
        return context

