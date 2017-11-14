from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from produit.models import *
from forms import *

def home(request):
    produits = FicheProduit.objects.all().order_by('-id')[:3]
    return render(request,"home.html", {'produits' : produits})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['sujet']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                messages.success(request, 'Probleme interne, impossible d\'envoyer un mail.')
                return render(request, "contact.html", {'form': form})
            messages.success(request, 'Envoie en cours.')
            return redirect('contact')
    return render(request, "contact.html", {'form': form})
