from django.shortcuts import render, redirect
from .cart import Cart
from django.views.generic import CreateView, TemplateView


    
class PaymentView(TemplateView):
    template_name = 'product/cart.html'

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return redirect(request.path_info)


