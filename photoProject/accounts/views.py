from django.views.generic import TemplateView

class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

