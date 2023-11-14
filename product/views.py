from django.shortcuts import render
from .cart import Cart

    
class PaymentView(TemplateView):
    template_name = 'course/cart.html'

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return redirect(request.path_info)


