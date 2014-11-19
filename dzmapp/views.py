from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from dzmapp.models import *
from dzmapp.forms import *
import datetime

def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def lookup(request):
    now = datetime.datetime.now()
    return render_to_response('lookup.html')

def record(request):
    def setRecordValue(request,p_v,p_m):
        p_r = P_Record(
            visit_date=request.POST['visit_date'],
            volunteer=p_v,
            map=p_m,
            map_x=request.POST['bmapx'],
            map_y=request.POST['bmapy'],
            street=request.POST['street'],
            num=request.POST['num'],
            response=request.POST['response'],
        )
        return p_r
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            volunteer_name = request.POST['volunteer']
            p_v = P_Volunteer.objects.get_or_create(name=volunteer_name)
            map_level1 = request.POST['map_level1']
            map_level2 = request.POST['map_level2']
            p_m = P_Map.objects.get_or_create(level1=map_level1, level2=map_level2)
            p_r = setRecordValue(request=request,p_v=p_v[0],p_m=p_m[0])
            p_r.save()
            return HttpResponseRedirect('/l')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecordForm()
    return render(request, 'record.html', {'form': form})

def new_record(request):
    return record(request)

def date_search_lookup(request,start_date,end_date):
    rs = P_Record.objects.all();
    return render_to_response('lookup.html',{'records':rs})

