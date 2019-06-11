from django.shortcuts import render
from .models import Movie

class IndexView(views.TemplateView):
    template = 'index.html'

    def get_context_data(self):
        context['movies'] = Movie.objects.all()
        return context
