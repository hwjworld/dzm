import datetime,time
import csv,codecs,io
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import loader, Context
from dzmapp.models import *
from dzmapp.forms import *


def home(request):
    now = datetime.datetime.now()
    html = "<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0'/></head><body>%s.<p><a href='/accounts/login'>login</a></p></body></html>" % now
    return HttpResponse(html)

def menu(request):
    return render_to_response('menu.html')

@login_required
def lookup(request):
    now = datetime.datetime.now()
    return render_to_response('lookup.html')

@login_required
def record(request):
    def setRecordValue(request,p_v,p_m,p_h):
        p_r = P_Record(
            visit_date=request.POST['visit_date'],
            volunteer=p_v,
            map=p_m,
            householder = p_h,
        )
        return p_r
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            volunteer_name = request.POST['volunteer']
            p_v = P_Volunteer.objects.get_or_create(name=volunteer_name)
            map_level1 = request.POST['map_level1'].upper()
            map_level2 = request.POST['map_level2']
            p_m = P_Map.objects.filter(level1=map_level1, level2=map_level2)
            p_h = P_householder.objects.get_or_create(name=request.POST['householder_name'],
                                                      sex=request.POST['householder_sex'],
                                                      street=request.POST['street'],
                                                      num=request.POST['num'],
                                                      response=request.POST['response'],
                                                      map_x=request.POST['bmapx'],
                                                      map_y=request.POST['bmapy'])
            p_r = setRecordValue(request=request,p_v=p_v[0],p_m=p_m[0],p_h=p_h[0])
            p_r.save()
            return HttpResponseRedirect('/l')
        else:
            return HttpResponseRedirect('/s')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecordForm()
    return render(request, 'record.html', {'form': form})

def new_record(request):
    return record(request)

def getTime(dtstr):
    time = datetime.datetime.strptime(dtstr, '%Y%m%d')
    return time.strftime('%Y-%m-%d')

@login_required
def date_search_lookup(request,start_date,end_date):
    rs = date_search(start_date,end_date)
    r_accept = 0
    r_reject = 0
    for r in rs:
        if r.householder.response == '1':
            r_accept = r_accept + 1
        else:
            r_reject = r_reject + 1
    rs_sum = {'a':r_accept,'r':r_reject}
    return render_to_response('lookup.html',{'records':rs,'rs_sum':rs_sum,'start_date':getTime(start_date),'end_date':getTime(end_date)})


def date_search(start_date,end_date):
    rs = P_Record.objects.filter(visit_date__lte=getTime(end_date),visit_date__gte=getTime(start_date)).order_by('visit_date')
    return rs


class UnicodeWriter(object):
    """
    Like UnicodeDictWriter, but takes lists rather than dictionaries.

    Usage example:

    fp = open('my-file.csv', 'wb')
    writer = UnicodeWriter(fp)
    writer.writerows([
        [u'Bob', 22, 7],
        [u'Sue', 28, 6],
        [u'Ben', 31, 8],
        # \xc3\x80 is LATIN CAPITAL LETTER A WITH MACRON
        ['\xc4\x80dam'.decode('utf8'), 11, 4],
    ])
    fp.close()
    """
    def __init__(self, f, dialect=csv.excel_tab, encoding="utf-16", **kwds):
        # Redirect output to a queue
        self.queue = io.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoding = encoding

    def writerow(self, row):
        # Modified from original: now using unicode(s) to deal with e.g. ints
        self.writer.writerow([str(s) for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        # data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = data.encode(self.encoding)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)



@login_required
def csv_export(request,start_date,end_date):
    rs = date_search(start_date,end_date)
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="workrecords_'+start_date+'-'+end_date+'.csv"'

    writer = UnicodeWriter(response, quoting=csv.QUOTE_ALL)
    writer.writerow(["日期","姓名","性别","胡同(街)","门牌","反应","义工"])
    for r in rs:
        writer.writerow([str(r.visit_date.strftime('%Y-%m-%d')),r.householder.name,
                         "男" if r.householder.sex=='1' else "女",r.householder.street,r.householder.num,
                         "续访" if r.householder.response=='1' else "拒绝",r.volunteer.name])

    return response
