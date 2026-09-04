from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Contact

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({},request))

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render({},request))

def contact(request):

    if request.method == 'POST':
        con_name = request.POST['contact_name']
        con_email = request.POST['contact_email']
        con_msg = request.POST['contact_msg']

        contact = Contact.objects.create(
            contact_name=con_name,
            contact_email=con_email,
            contact_msg=con_msg)
        contact.save()
        
    template = loader.get_template("contact.html")
    return HttpResponse(template.render({},request))