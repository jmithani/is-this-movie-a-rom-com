from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Movie

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context
