from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers









urlpatterns = [
    path('', views.index, name="index"),
    path('stripeapproach', views.approach, name="stripeapproach"),
    path('approach', views.generalapproach, name="approach"),
    path('startups', views.startups, name="startups"),
    path('enterprises', views.enterprises, name="enterprises"),
    path('contact', views.contact, name="contact"),
    path('casestudies', views.CaseList.as_view(), name="casestudies"),
    path('case/<pk>', views.CaseDetail.as_view(), name="casedetail"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)