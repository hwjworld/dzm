import string
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from dzmapp.models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def mapedit(request):
    return render_to_response('maps/map_base.html')


def check(request):
    maps = P_Map.objects.order_by('level1','level2')
    print (maps)
    return render_to_response('maps/check.html',{'maps':maps})

def manage(request):
    return render_to_response('maps/edit.html')

@csrf_exempt
def savemap(request):
    if request.method == 'POST':
        try:
            p_m = P_Map.objects.get_or_create(level1=request.POST["level1"].upper(),
                        level2=request.POST["level2"].upper())[0]
            p_m.mapx=request.POST["mapx"]
            p_m.mapy=request.POST["mapy"]
            p_m.mappolyline=request.POST["polyline"]
            p_m.zoom=request.POST["zoom"]
            p_m.save()
        except Exception as e:
            print (e)
            return HttpResponse("失败修改.", content_type="text/plain")
        return HttpResponse("成功修改.", content_type="text/plain")
    else:
        return HttpResponse("Thanks.", content_type="text/plain")

@csrf_exempt
def deletemap(request):
    if request.method == 'POST':
        try:
            p_m = P_Map.objects.filter(level1=request.POST["level1"].upper(),
                        level2=request.POST["level2"].upper())
            p_m.delete()
        except:
            return HttpResponse("错了.", content_type="text/plain")
        return HttpResponse("成功.", content_type="text/plain")
    else:
        return HttpResponse("Thanks.", content_type="text/plain")