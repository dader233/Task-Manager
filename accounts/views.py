# accounts/views.py
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    first_name = forms.CharField(max_length=30, required=True, label='Имя')
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'email')

class LandingView(TemplateView):
    template_name = 'accounts/landing.html'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        return reverse_lazy('task_list')


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('landing')
  