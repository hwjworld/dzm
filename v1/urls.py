from django.conf.urls import patterns, include, url
from django.contrib import admin
from dzmapp.apps.map.views import *
from dzmapp.apps.map.mapop import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dzmapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu$', 'dzmapp.views.menu', name='menu'),
)
# volunteer
urlpatterns += patterns('',
    url(r'^accounts/init_users', 'dzmapp.apps.volunteer.views.init_users', name="init_users"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^accounts/login_ajax$', 'dzmapp.apps.volunteer.views.login_ajax', name="login_ajax"),
)
# maps
urlpatterns += patterns('dzmapp.apps.map.views',
    url(r'^map/$', 'mapedit'),
    url(r'^map/check$', 'check'),
    url(r'^map/manage$', 'manage'),
    url(r'^map/s', 'savemap'),
    url(r'^map/d', 'deletemap'),

)
# -1 = list
# 0 = minimun value
urlpatterns += patterns('',
    url(r'^map/level1/$', 'dzmapp.apps.map.mapop.getMap',{'level1':'-1','level2':'-1'}),
    url(r'^map/level1/(?P<level1>\w{1})$', 'dzmapp.apps.map.mapop.getMap',{'level2':'0'}),
    url(r'^map/level1/(?P<level1>\w{1})/level2/$', 'dzmapp.apps.map.mapop.getMap',{'level2':'-1'}),
    url(r'^map/level1/(?P<level1>\w{1})/level2/(?P<level2>\w+)', 'dzmapp.apps.map.mapop.getMap'),
)
# lookup
urlpatterns += patterns('',
    url(r'^l$', 'dzmapp.views.lookup'),
    # url(r'^l/(?P<year>\d{4})/$', 'dzmapp.views.year_lookup'),
    # url(r'^l/(?P<month>\d{6})/$', 'dzmapp.views.month_lookup'),
    # url(r'^l/(?P<day>\d{8})/$', 'dzmapp.views.day_lookup'),
    url(r'^l/(?P<start_date>\d{8})-(?P<end_date>\d{8})$', 'dzmapp.views.date_search_lookup'),
    url(r'^csv/(?P<start_date>\d{8})-(?P<end_date>\d{8})$', 'dzmapp.views.csv_export'),
)
# add record
urlpatterns += patterns('',
    url(r'^r$', 'dzmapp.views.new_record'),
)

# mobile
urlpatterns += patterns('',
    url(r'^m$', 'dzmapp.apps.mobile.views.m', name="m"),
)
# user
urlpatterns += patterns('',
    url(r'^users/$', 'dzmapp.apps.volunteer.views.users', name="users"),
    url(r'^/users/add$', 'dzmapp.apps.volunteer.views.user_add', name="user_add"),

)