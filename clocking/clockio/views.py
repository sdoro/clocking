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

def checkin(request):
    tmp = {'Cognome': "Rossi", 'Nome': "Pierino", 'CheckPoint': "LAM2", 'Ora': datetime.now() }
    return render(request, 'checkin.html', {'cntx': tmp})

def checkout(request):
    tmp = {'Cognome': "Rossi", 'Nome': "Pierino", 'CheckPoint': "LAM2", 'Ora': datetime.now(), 'Durata': 340 }
    return render(request, 'checkout.html', {'cntx': tmp})
