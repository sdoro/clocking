from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<checkpoint_id>[0-9]+)/checkin$', views.checkin),
    url(r'^(?P<checkpoint_id>[0-9]+)/checkout$', views.checkout),
]
