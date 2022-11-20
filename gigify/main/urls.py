from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('approach', views.approach, name="approach"),
    path('startups', views.startups, name="startups"),
    path('enterprises', views.enterprises, name="enterprises"),
    path('contact', views.contact, name="contact"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)