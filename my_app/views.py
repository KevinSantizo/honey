from django.http import HttpResponse
import time
import json
import libhoney
from rest_framework import generics, views, response, status, filters, viewsets

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world!")


libhoney.init(writekey='cQDbjNT0FAoOYWFA5XJwBC', dataset='telemetry')


""" 
def log_event(name, message, view, request_type, status_code=None, email=None, error=None, metadata=None):
    event = libhoney.new_event()
    payload = {
        'status': 'error' if error  else 'success',
        'status_code': status_code,
        'error': error,
        'email': email,
        'name': name,
        'message': message,
        'view': view,
        'request_type': request_type,
        'metadata': json.dumps(metadata) if metadata else None,
    }

    event.add(payload)
    event.send()

    return HttpResponse(payload, request_type, status_code)


# 1. Basic successful login
log_event('login', 'User logged in successfully', 'login_page', 'POST', status_code=200, email='user@example.com')

# 2. Failed login attempt
log_event('login_failure', 'Invalid credentials', 'login_page', 'POST', status_code=401, error='Authentication failed')

# 3. User registration
log_event('register', 'New user registered', 'registration_page', 'POST', status_code=201, email='newuser@example.com')

# 4. Password reset request
log_event('password_reset', 'Password reset requested', 'forgot_password_page', 'POST', email='user@example.com')

# 5. View product page
log_event('view_product', 'User viewed product', 'product_page', 'GET', metadata={'product_id': '12345'})

# 6. Add to cart
log_event('add_to_cart', 'Product added to cart', 'product_page', 'POST', metadata={'product_id': '12345', 'quantity': 2})

# 7. Checkout process
log_event('checkout', 'User initiated checkout', 'checkout_page', 'POST', email='user@example.com', metadata={'total_amount': 99.99})

# 8. Order confirmation
log_event('order_confirmation', 'Order placed successfully', 'order_confirmation_page', 'GET', status_code=200, email='user@example.com', metadata={'order_id': 'ORD-123456'})

# 9. Customer support ticket
log_event('support_ticket', 'New support ticket created', 'support_page', 'POST', email='user@example.com', metadata={'ticket_id': 'TICKET-789'})

# 10. API call error
log_event('api_error', 'External API call failed', 'backend_process', 'GET', status_code=500, error='API timeout', metadata={'api_endpoint': 'https://api.example.com/data'})



count = 0
while True:
    count = count + 1
    time.sleep(1)
    print(f'{count} seconds elapsed')
    if count == 10:
        break
"""


class SendHoneyCombData(views.APIView):
    def post(self, request):
        req = json.loads(self.request.body)
        data = req
        event = libhoney.new_event()
        payload = data
        count = 0
        while True:
            count = count + 1
            time.sleep(1)
            print(f'{count} seconds elapsed')
            if count == 10:
                break
        event.add(payload)
        event.send()
        return HttpResponse(json.dumps({'result': True, 'data': data}), content_type='application/json')
