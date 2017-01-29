from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

def greets(request):
    ora = str(datetime.now())
    html = "<html><body>" + \
     "Sistema di rilevazione presenze Istituto C.Zuccante " + \
     "<br>" + ora + \
     "</body></html>"
    return HttpResponse(html)

def clockin(request):
    pass

def clockout(request):
    pass
