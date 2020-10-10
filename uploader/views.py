from django.contrib.messages.api import error
from django.shortcuts import render
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")


def uploader(request):
    if request.method == 'POST':
        if request.POST.get('sender') and request.FILES.get('myfile'):
            person_resource = PersonResource()
            dataset = Dataset()
            new_person = request.FILES['myfile']
            sender = request.POST['sender']

            if not new_person.name.endswith('xlsx'):
                error = {
                    "error": 'Your file is not a valid excelsheet.'
                }
                return render(request, "dashboard.html", error)

            imported_data = dataset.load(new_person.read(), format="xlsx")
            for data in imported_data:
                value = Person(
                    data[0],
                    sender,
                    data[2],
                    data[3],
                    data[4],
                    data[5]
                )
                value.save()
                
            messages.success(
                    request, "We have successfully uploaded the data on our server.")
            return render(request, "dashboard.html")
        else:
            error = {
                "error": 'One or more fields is missing.'
            }
            return render(request, "dashboard.html", error)
    return render(request, "dashboard.html")


def add_form(request):
    if request.method == 'POST':
        if request.POST.get('sender') and request.POST.get('receiver') and request.POST.get('email') and request.POST.get('bday'):
            sender = request.POST['sender']
            receiver = request.POST['receiver']
            email = request.POST['email']
            bday = request.POST['bday']
            year_now = int(datetime.now().strftime("%Y"))-1
            person = Person(
                sender=sender,
                receiver=receiver,
                email=email,
                bday=bday,
                year=year_now
            )
            person.save()
            messages.success(
                    request, "We have successfully added the data on our server.")
            return render(request, "form.html")
        else:
            error = {
                "error": 'One or more fields is missing.'
            }
            return render(request, "form.html", error)
    return render(request, "form.html")