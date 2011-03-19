from django.conf.urls.defaults import *

# enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^fleamarket/', include('fleamarket.foo.urls')),
     (r'^listings/', include('fleamarket.listings.urls')),

    # enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
