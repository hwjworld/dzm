import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from dzmapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
@login_required
def m(request):
    #html = "<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0'/></head><body>开发中,返回<a href='/l'>主版本</a>.</body></html>"
    #return HttpResponse(html)
    l1 = request.POST.get('l1','A')
    l2 = request.POST.get('l2','0')
    return render_to_response("mobile/m_record.html",{'level1':l1, 'level2':l2})

def m1(request,level1,level2):
    volunteer_name=request.POST.get('v','')
    success=request.POST.get('success','0')
    #html = "<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0'/></head><body>开发中,返回<a href='/l'>主版本</a>.</body></html>"
    #return HttpResponse(html)
    return render_to_response("mobile/m_record.html",{'level1':level1, 'level2':level2,'volunteer_name':volunteer_name,'success':success})

@login_required
def ml(request):
    l1 = request.POST.get('l1','A')
    l2 = request.POST.get('l2','0')
    return render_to_response("mobile/m_lookup.html",{'level1':l1, 'level2':l2})

def getTime(dtstr):
    time = datetime.datetime.strptime(dtstr, '%Y%m%d')
    return time.strftime('%Y-%m-%d')

@login_required
def date_search_lookup(request,start_date,end_date):
    rs = date_search(start_date,end_date)
    rs_sum = date_search_with_area_rs_sum(rs)
    # c = RequestContext(request, { 'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})
    # return render('lookup.html',c)

    return render_to_response('mobile/m_lookup.html',{'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})


def date_search(start_date,end_date):
    rs_v = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=getTime(start_date),
                                 householder__response=2).order_by('visit_date')  # query visited records

    oneyear_ago = datetime.datetime.strptime(end_date, '%Y%m%d')-datetime.timedelta(days=365)
    rs_a_r = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=oneyear_ago,
                                 householder__response__in=[1,0]).order_by('visit_date') #query accept and refused records
    return rs_v | rs_a_r # combine two queryset


@login_required
def date_search_with_area_lookup(request,start_date,end_date,level1,level2):
    rs = date_search_with_area(start_date,end_date,level1,level2)
    rs_sum = date_search_with_area_rs_sum(rs)
    # c = RequestContext(request, { 'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})
    # return render('lookup.html',c)

    return render_to_response('mobile/m_lookup.html',{'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date), 'level1':level1, 'level2':level2})


def date_search_with_area(start_date,end_date,map_level1,map_level2):
    oneyear_ago = datetime.datetime.strptime(end_date, '%Y%m%d') - datetime.timedelta(days=365)
    if(map_level2 == '0'):
        map_ids = P_Map.objects.filter(level1=map_level1)
        rs_v = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=getTime(start_date),
                                     map_id__in=map_ids, householder__response=2).order_by('visit_date')

        rs_a_r = P_Record.objects.filter(visit_date__lte=getTime(end_date), visit_date__gte=oneyear_ago,
                                         map_id__in=map_ids, householder__response__in=[1, 0])\
            .order_by('visit_date')  # query accept and refused records
        rs = rs_v | rs_a_r

    else:
        map_id = P_Map.objects.get(level1=map_level1, level2=map_level2)
        rs_v = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=getTime(start_date),
                                       map_id=map_id, householder__response=2).order_by('visit_date')
        rs_a_r = P_Record.objects.filter(visit_date__lte=getTime(end_date), visit_date__gte=oneyear_ago,
                                         map_id=map_id, householder__response__in=[1, 0])\
            .order_by('visit_date')  # query accept and refused records
        rs = rs_v | rs_a_r
    return rs

def date_search_with_area_rs_sum(rs):
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
    return rs_sum


@csrf_exempt
@login_required
def date_search_with_area_lookup_json(request,start_date,end_date,level1,level2):
    from datetime import datetime
    from django.utils.dateformat import DateFormat
    from django.utils.formats import get_format

    rs = date_search_with_area(start_date,end_date,level1,level2)
    rs_sum = date_search_with_area_rs_sum(rs)
    rs_json = []
    for v in rs:
        rs_json.append({"map_x":v.householder.map_x, "map_y":v.householder.map_y,"name":v.householder.name,
                        "num":v.householder.num,"response":v.householder.response,
                        "visit_date":DateFormat(v.visit_date).format('Y - m - d D')})
        # [{{}}, {{}},
        #  "{{ v.householder.name }},{{v.householder.num}},{% ifequal v.householder.response "1
        #  " %}<b>续访</b>{% endifequal %}{% ifequal v.householder.response "0
        #  " %}<b>拒绝</b>{% endifequal %}{% ifequal v.householder.response "2
        #  " %}<b>拜访过</b>{% endifequal %}, {{v.visit_date|date:"Y - m - d D"}}来过."],

    # c = RequestContext(request, { 'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})
    # return render('lookup.html',c)
    return JsonResponse(rs_json, safe=False)
