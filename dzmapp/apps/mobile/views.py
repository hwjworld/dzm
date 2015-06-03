import datetime,time
import csv,codecs,io
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import loader, Context
from dzmapp.models import *
from dzmapp.forms import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect,ensure_csrf_cookie

@csrf_exempt
@login_required
def m(request):
    #html = "<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0'/></head><body>开发中,返回<a href='/l'>主版本</a>.</body></html>"
    #return HttpResponse(html)
    return render_to_response("mobile/m_record.html")
