from django.shortcuts import render

from django.views.generic import ListView

from . import models

class SearchResultsView(ListView):
    model = models.Job
    template_name = 'vacancy/search_results.html'

def vacancy(request):
    return render(request, 'vacancy/search_results.html')