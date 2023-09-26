from django.shortcuts import redirect, render
from django.template import base
from twilio.rest import Client
from .forms import *
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
import stripe
from django.template.loader import render_to_string
from django.db.models import Q
import lyricsgenius
from django.http import JsonResponse
import requests



# Create your views here.


def index(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    context['cases'] = Case.objects.all()



    return render(request, 'index.html', context)

@login_required
def dashboard(request):
    context = {}
    context['tasks'] = Task.objects.filter(user=request.user).order_by('position')[:2]
    context['deliverables'] = Deliverable.objects.filter(user=request.user)
    context['messages'] = Message.objects.filter(user=request.user)[:5]
    context['invoices'] = Invoice.objects.filter(user=request.user)[:5]
    return render(request, 'dashboard.html', context)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')
    

def booking(request):
    context = {}
    context['casestudies'] = Case.objects.all()
    return render(request, 'booking.html', context)

def payment(request, amt):
    amount = amt
    link = requests.get(f"https://retainlysms-backend.herokuapp.com/api/stripe/afterpay/{amount}")
    linkredirect = link.json()['sessionURL']
    return HttpResponseRedirect(linkredirect)


def approach(request):
    context = {}
    return render(request, 'approach.html', context)

def startups(request):
    context = {}
    return render(request, 'startups.html', context)

def enterprises(request):
    context = {}
    return render(request, 'enterprise.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def generalapproach(request):
    context = {}
    return render(request, 'generalapproach.html', context)

class CaseList(ListView):
    model = Case
    template_name = 'casestudies.html'

class CaseDetail(DetailView):
    model = Case
    template_name = 'casedetail.html'

