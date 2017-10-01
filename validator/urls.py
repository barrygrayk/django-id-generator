
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
from .views import PersonCreateView,PersonDetailView,IdValidateView

from django.contrib.auth.views  import LoginView



urlpatterns = [
    url(r'^create/$', PersonCreateView.as_view(),name ='genarate_id'),
    url(r'^(?P<pk>\d+)/$', PersonDetailView.as_view(), name='details'),
        url(r'^validate/$', IdValidateView.as_view(), name='checkid'),

]
