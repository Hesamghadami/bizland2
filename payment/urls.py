from django.urls import path
from .views import *

app_name = 'payment'

from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
    path('error-payment/', views.connection_error , name='connection_error'),
    path('error-payment-zarrinpal/', views.error , name='payment_error_zarrinpal'),
    path('error-payment-zarrinpal/', views.confirmation , name='confirmation'),
    path('error-payment-zarrinpal/', views.confirmation_error , name='confirmation-error'),
    
]