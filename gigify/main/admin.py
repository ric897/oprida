from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Case)
admin.site.register(Invoice)
admin.site.register(Task)
admin.site.register(Deliverable)
admin.site.register(Message)
