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

@login_required
def ml(request):
    return render_to_response("mobile/m_lookup.html")

def getTime(dtstr):
    time = datetime.datetime.strptime(dtstr, '%Y%m%d')
    return time.strftime('%Y-%m-%d')

@login_required
def date_search_lookup(request,start_date,end_date):
    rs = date_search(start_date,end_date)
    r_accept = 0
    r_reject = 0
    r_visited = 0
    for r in rs:
        if r.householder.response == '1':
            r_accept = r_accept + 1
        elif r.householder.response == '0':
            r_reject = r_reject + 1
        else:
            r_visited = r_visited + 1
    rs_sum = {'a':r_accept,'r':r_reject,'v':r_visited}
    # c = RequestContext(request, { 'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})
    # return render('lookup.html',c)

    return render_to_response('mobile/m_lookup.html',{'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})


def date_search(start_date,end_date):
    rs = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=getTime(start_date)).order_by('visit_date')
    return rs


@login_required
def date_search_with_area_lookup(request,start_date,end_date,level1,level2):
    rs = date_search_with_area(start_date,end_date,level1,level2)
    r_accept = 0
    r_reject = 0
    r_visited = 0
    for r in rs:
        if r.householder.response == '1':
            r_accept = r_accept + 1
        elif r.householder.response == '0':
            r_reject = r_reject + 1
        else:
            r_visited = r_visited + 1
    rs_sum = {'a':r_accept,'r':r_reject,'v':r_visited}
    # c = RequestContext(request, { 'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})
    # return render('lookup.html',c)

    return render_to_response('mobile/m_lookup.html',{'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date), 'level1':level1, 'level2':level2})


def date_search_with_area(start_date,end_date,map_level1,map_level2):
    if(map_level2 == '0'):
        map_ids = P_Map.objects.filter(level1=map_level1)
        rs = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=getTime(start_date),map_id__in=map_ids).order_by('visit_date')
    else:
        map_id = P_Map.objects.get(level1=map_level1, level2=map_level2)
        rs = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=getTime(start_date),map_id=map_id).order_by('visit_date')

    return rs
