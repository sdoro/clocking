from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clockin$', views.clockin),
    url(r'^clockout$', views.clockout),
]