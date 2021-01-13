from django.shortcuts import render, HttpResponse, redirect
from uploader.models import Person
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from uploader.views import home
from datetime import datetime
from django.http import request


# Create your views here.
def sender(request):
    today = datetime.now().strftime("%d-%m")
    year_now = datetime.now().strftime("%Y")
    data = Person.objects.all()
    for item in data.values('id', 'sender', 'receiver', 'bday', 'email', 'year'):
        bday = item['bday'].strftime("%d-%m")
        receiver_email = item['email']
        id_user = item['id']
        year_in_db = item['year']
        sender = item['sender'].split(" ")[0]
        receiver = item['receiver'].split(" ")[0]
        if bday == today and year_in_db < int(year_now):
            context = {
                "receiver": receiver,
                "sender": sender,
            }
            print(f"Birthday Details : {context}")
            html_content = render_to_string("email.html", context)
            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives(
                f"Happy Birthday {receiver}",
                text_content,
                "PyWisher <pywisher@gmail.com>",
                [receiver_email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            user = Person.objects.get(id=id_user)
            user.year = year_now
            user.save()
    return redirect(home)


def email_temp(request, sender=None, receiver=None):
    if not sender or sender == None or not receiver or receiver == None:
        return render(request, "index.html")
    else:
        context = {
            "sender": sender,
            "receiver": receiver
        }
        return render(request, "wish.html", context)


def Task():
    return sender(request)
