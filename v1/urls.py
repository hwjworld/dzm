from django.conf.urls import include, url
from django.contrib import admin
from dzmapp import views as dzmapp_view
from dzmapp.apps.volunteer import views as volunteer_views
from dzmapp.apps.map import views as map_view
from dzmapp.apps.map import mapop as map_op
from dzmapp.apps.mobile import views as mobile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    url(r'^$', dzmapp_view.home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^menu$', dzmapp_view.menu, name='menu'),

# volunteer
    url(r'^accounts/init_users', volunteer_views.init_users, name="init_users"),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', auth_views.logout_then_login),
    url(r'^accounts/login_ajax$', volunteer_views.login_ajax, name="login_ajax"),

# maps
    url(r'^map/$', map_view.mapedit),
    url(r'^map/check$', map_view.check),
    url(r'^map/manage$', map_view.manage),
    url(r'^map/s', map_view.savemap),
    url(r'^map/d', map_view.deletemap),


# -1 = list
# 0 = minimun value
    url(r'^map/level1/$', map_op.getMap,{'level1':'-1','level2':'-1'}),
    url(r'^map/level1/(?P<level1>\w{1})$', map_op.getMap,{'level2':'0'}),
    url(r'^map/level1/(?P<level1>\w{1})/level2/$', map_op.getMap,{'level2':'-1'}),
    url(r'^map/level1/(?P<level1>\w{1})/level2/(?P<level2>\w+)', map_op.getMap),

# lookup
    url(r'^l$', dzmapp_view.lookup),
    # url(r'^l/(?P<year>\d{4})/$', 'dzmapp_view.year_lookup'),
    # url(r'^l/(?P<month>\d{6})/$', 'dzmapp_view.month_lookup'),
    # url(r'^l/(?P<day>\d{8})/$', 'dzmapp_view.day_lookup'),
    url(r'^l/(?P<start_date>\d{8})-(?P<end_date>\d{8})$', dzmapp_view.date_search_lookup),
    url(r'^csv/(?P<start_date>\d{8})-(?P<end_date>\d{8})$', dzmapp_view.csv_export),

# add record
    url(r'^r$', dzmapp_view.new_record),


# mobile
    url(r'^m$', mobile_view.m, name="m"),
    url(r'^m/(?P<level1>\w{1})/(?P<level2>\w{1})', mobile_view.m1, name="m1"),
    url(r'^ml$', mobile_view.ml, name="m_lookup"),
    url(r'^ml/(?P<start_date>\d{8})-(?P<end_date>\d{8})$', mobile_view.date_search_lookup),
    url(r'^ml/(?P<start_date>\d{8})-(?P<end_date>\d{8})/(?P<level1>\w{1})/(?P<level2>\w{1})$', mobile_view.date_search_with_area_lookup),
    url(r'^api/ml/(?P<start_date>\d{8})-(?P<end_date>\d{8})/(?P<level1>\w{1})/(?P<level2>\w{1})$', mobile_view.date_search_with_area_lookup_json),

# user
    url(r'^users/$', volunteer_views.users, name="users"),
    url(r'^users/add$', volunteer_views.user_add, name="user_add")

]