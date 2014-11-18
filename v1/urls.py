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
    url(r'^r$', 'dzmapp.views.record'),
    # url(r'^lookup/$', 'views.this_month'),
    # url(r'^lookup/(?P<year>\d{4})/$', views.year_lookup),
    # url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_lookup),
    # url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.day_lookup),
)
