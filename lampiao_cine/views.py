from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, 'index.html')

class AboutPageView(TemplateView):
    template_name = "about.html"