import string
import json
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from dzmapp.models import *

#返回polyline or list
@csrf_exempt
def getMap(request,level1,level2):
    level1 = level1.upper()
    level2 = level2.upper()
    # return level1 list
    if level1=='-1' and level2=='-1':
        ps = P_Map.objects.order_by('level1')
        rs = []
        for i in ps:
            if i.level1 not in rs:
                rs.append(i.level1)
        return HttpResponse(json.dumps(rs))
    # return level1 and level2 min value polyline
    elif level2=='0':
        ps = P_Map.objects.filter(level1=level1).order_by('level2')
        if ps.count()>0:
            return HttpResponse(ps[0].mappolyline)
        else:
            return HttpResponse([])
    # return level1 and level2 list
    elif level2=='-1':
        ps = P_Map.objects.filter(level1=level1).order_by('level2')
        rs = []
        for i in ps:
            if i.level2 not in rs:
                rs.append([i.level2,i.mappolyline])
        return HttpResponse(json.dumps(rs))
    # return polyline
    else:
        ps = P_Map.objects.filter(level1=level1,level2=level2)
        if ps.count()>0:
            return HttpResponse(ps[0].mappolyline)
        else:
            return HttpResponse([])