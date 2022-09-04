from django.shortcuts import render

from django.views.generic import ListView

from . import models

class SearchResultsView(ListView):
    model = models.Job
    template_name = 'job_search/search_results.html'