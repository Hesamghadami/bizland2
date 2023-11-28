from django.shortcuts import render ,redirect,request
from django.views.generic import ListView
from .forms import *
from .models import *
from django.contrib import messages

class HomeListView(ListView):
    template_name = 'root/index.html'
    context_object_name = 'service'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teammember'] = Teammember.objects.filter(status=True)
        context['portfolio'] = Portfolio.objects.filter(status=True)
        context['price'] = Price.objects.filter(status=True)
        return context    
    
    def Post(self, *args, **kwargs):
        form = NewsLetterForm(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your email submited successfully')
            return redirect('root:home')
        
        else:
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:home')    