from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dzmapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
# lookup
urlpatterns += patterns('',
    url(r'^l$', 'dzmapp.views.lookup'),
    # url(r'^l/(?P<year>\d{4})/$', 'dzmapp.views.year_lookup'),
    # url(r'^l/(?P<month>\d{6})/$', 'dzmapp.views.month_lookup'),
    # url(r'^l/(?P<day>\d{8})/$', 'dzmapp.views.day_lookup'),
    url(r'^l/(?P<start_date>\d{8})-(?P<end_date>\d{8})$', 'dzmapp.views.date_search_lookup'),
)
# add record
urlpatterns += patterns('',
    url(r'^r$', 'dzmapp.views.new_record'),
)
