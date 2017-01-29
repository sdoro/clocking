from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^checkin$', views.checkin),
    url(r'^checkout$', views.checkout),
]