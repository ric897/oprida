from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget
from .models import *

class OpenAI(forms.Form):
    input_text = forms.CharField(label="Ask us anything about our business!", widget=forms.Textarea(attrs={'class':'text-xl my-3 rounded-xl text-black transition ease-in-out w-full bg-white'}))