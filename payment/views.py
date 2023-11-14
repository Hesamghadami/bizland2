from django.conf import settings
import requests
import json
from django.shortcuts import get_object_or_404, redirect, render
from order.models import OrderBy

#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"


phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/payment/verify/'

def send_request(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(OrderBy, id=order_id)
    fee = order.get_total_price()*10 # change toman to rial
    description = f"{order.id} : {order.user.email}"
    request_data = {
        "MerchantID": settings.MERCHANT,
        "Amount": fee,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    request_data = json.dumps(request_data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(request_data))}
    response = requests.post(ZP_API_REQUEST, data=request_data,headers=headers, timeout=10)#receive authority # no call back . just receive data from api
    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            order.zarinpal_authority = response['Authority']
            order.save()
            return redirect(ZP_API_STARTPAY + response['Authority'])#check authority an go to callback
        else:
            return redirect("payment:payment_error_zarrinpal")
    else:
        return redirect("payment:connection_error")
        

def verify(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(OrderBy, id=order_id)
    fee = order.get_total_price()*10 # change toman to rial
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": fee,
        "Authority": request.GET.get("Authority"),
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            order.zarinpal_refid = response['RefID']
            order.zarinpal_data = response['data']
            order.save()
            return redirect("payment:confirmation")
        else:
            return redirect("payment:confirmation-error")

def error(request):
    return render(request, 'payment/error.html')

def connection_error(request):
    return render(request, 'payment/connection_error.html')

def confirmation(request):
    del request.session['order_id']
    return render(request, 'payment/confirmation.html')

def confirmation_error(request):
    return render(request, 'payment/confirmation_error.html')
