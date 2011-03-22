from django.conf.urls.defaults import *
from django.contrib.auth.models import User
#from django.views.generic import list_detail, create_update
from listings.models import Item
import views
from forms import NewItemForm

all_sellers = {
    # TODO: Filter out staff from this query
    'queryset': User.objects.all(),
}

all_items = {
    'queryset': Item.objects.all(),
}

my_listings_dict = {
        # TODO: How to feed in the proper seller id to this query
    'queryset': Item.objects.filter(seller__exact=4),
}

item_info = {
    'model': Item,
}

urlpatterns = patterns('',
        
    ########################################
    # Seller URLs
    ########################################

    #(r'^$', 'django.views.generic.list_detail.object_list', all_items),
    #(r'^$', 'django.views.generic.list_detail.object_list', my_listings_dict),
    (r'^$', views.list),
    (r'^print/$', views.print_friendly),
    #(r'^$', 'django.views.generic.list_detail.object_list', my_listings_dict),
    
    #(r'^new/$', 'django.views.generic.create_update.create_object', item_info),
    (r'^new/$', views.new),

    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', all_items),
    (r'^(?P<object_id>\d+)/edit$', 'django.views.generic.create_update.update_object', 
        {
            'form_class': NewItemForm,
            #'model': Item,
        }
    ),

    # We're naming this 'item_results'
    url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(all_items, template_name='items/results.html'), 'item_results'),

    ########################################
    # Cashier URLs
    ########################################
    (r'^cash_register/$', views.cash_register),
    #(r'^checkin/$', views.checkin),
    (r'^checkin/$', views.checkin_list),
    #(r'^checkin/$', 'django.views.generic.list_detail.object_list', all_sellers),
    (r'^checkin/(?P<object_id>\d+)$', views.checkin),
)
