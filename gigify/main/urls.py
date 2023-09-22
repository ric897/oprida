from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.contrib.auth.views import LogoutView









urlpatterns = [
    path('', views.index, name="index"),
    path('stripeapproach', views.approach, name="stripeapproach"),
    path('approach', views.generalapproach, name="approach"),
    path('startups', views.startups, name="startups"),
    path('enterprises', views.enterprises, name="enterprises"),
    path('contact', views.contact, name="contact"),
    path('casestudies', views.CaseList.as_view(), name="casestudies"),
    path('case/<pk>', views.CaseDetail.as_view(), name="casedetail"),
    path('login', views.CustomLoginView.as_view(), name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', LogoutView.as_view(), name='logout'),
     path('info/', views.booking, name='booking'),




]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)