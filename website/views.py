from django.shortcuts import render
from .models import SignUp,Contact
# Create your views here.
import time


def indexfunc(request):
    if request.method == 'GET':
        return render(request, 'website/index.html', {})
    elif request.method == 'POST':
        # Sign up
        signup = request.POST.get('email2')
        s = SignUp(email = signup)
        s.save()

        # Contact

        customer_name = request.POST.get('name')
        customer_email = request.POST.get('email')
        customer_contact = request.POST.get('contactno')
        customer_message = request.POST.get('message')
        c = Contact(name = customer_name, email=customer_email, contact_no = customer_contact, drop_us_a_line = customer_message)
        c.save()
        time.sleep(5)
        return render(request, 'website/index.html', {})

