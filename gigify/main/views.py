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

# Create your views here.


def index(request):
    context = {}
    context['cases'] = Case.objects.all()

    if request.method == 'Post':


        form = OpenAI(request.POST)

        openai.api_key = "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"

        # Use the OpenAI API to generate some text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Once upon a time, in a land far, far away, there was a",
            max_tokens=100,
            n=1,
            temperature=0.5,
        )

        context['form'] = form
        context['text'] = response

        return render(request, 'index.html', context)
    
    else:

        form = OpenAI
        context['form'] = form

        return render(request, 'index.html', context)

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

