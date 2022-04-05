from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from .forms import UserForm

from django.urls import reverse_lazy

from .models import Profile

# Create your views here.
class UserCreate(CreateView):
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        url = super().form_valid(form)
        Profile.objects.create(user=self.object)

        return url

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = 'User Signup'
        context['button'] = 'signup'


        return context


class ProfileUpdate(UpdateView):
    template_name = 'form.html'
    model = Profile
    fields = ['name', 'lastName', 'birthDate' ,'city', 'country', 'phone']
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Profile, user=self.request.user)
        return self.object
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = 'Profile'
        context['button'] = 'Update'


        return context

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'