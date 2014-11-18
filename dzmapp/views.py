from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def lookup(request):
    now = datetime.datetime.now()
    return render_to_response('lookup.html')

def record(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return render_to_response('record.html')
