from django.shortcuts import render ,redirect
from django.views.generic import ListView
from .models import *


class HomeListView(ListView):
    template_name = 'root/index.html'
    context_object_name = 'service'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teammember'] = Teammember.objects.filter(status=True)
        context['portfolio'] = Portfolio.objects.filter(status=True)
        context['price'] = Price.objects.filter(status=True)
        return context    
    
