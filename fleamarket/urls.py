from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
import views

# enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Login/Logout
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', views.profile),

    # Listings
    (r'^listings/', include('fleamarket.listings.urls')),

    # admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # admin:
    (r'^admin/', include(admin.site.urls)),
)
