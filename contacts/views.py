
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
# @login_required
def contact(request) :
    if request.method == 'POST':
        listing = request.POST["listing"]
        listing_id = request.POST["listing_id"]
        name = request.POST["name"].capitalize()
        email = request.POST["email"]
        phone = request.POST["phone"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]
        message = request.POST["message"]

        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone
        ,user_id=user_id,message=message)

        contact.save()
        # send email 
        # email config (https://docs.djangoproject.com/en/3.2/topics/email/) this django decument
        # also there are setting in the settings file you have to take a look there 
        send_mail(
            'sending the first email from django',
            'this email for to inform you that you are so good and amazing programer',
            'mahmoudhaleem200@gmail.com',
            [realtor_email,'mahmoudhaleem100@gmail.com'],
            fail_silently=False
        )

        return redirect("dashboard")